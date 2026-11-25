#!/usr/bin/env python3
"""Regenerate the reference pages of this site from a release checkout of AthenaK.

The text of the scheme lives with the code, in docs/vet_clean/*.md and tests/vet_clean/README.md
(updated in the same commit as the code). This script converts it to reStructuredText with
pandoc and splits it into the pages of this site. Pages it writes start with a "generated"
comment; edit the Markdown in the code repository, not those pages. The hand-written pages
(index, gallery, faq) are not touched.

    pip install -r tools/requirements-sync.txt
    python tools/sync_from_code.py /path/to/athenak

Every text fix below must match exactly once; a fix that no longer matches stops the script,
so a change of the Markdown is noticed instead of silently producing a broken page.
"""
import os
import re
import shutil
import subprocess
import sys

import pypandoc

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'source')

PAGE = {  # Markdown file -> page, for links
    'QUICKSTART.md': 'quickstart', 'BUILD.md': 'build', 'RUN.md': 'running_the_code',
    'KEYS.md': 'keys', 'OUTPUTS.md': 'outputs', 'SCHEME.md': 'scheme', 'STARS.md': 'stars',
    'PERFORMANCE.md': 'performance', '../../tests/vet_clean/README.md': 'tests',
    '../../tests/vet_clean/notebooks/README.md': 'gallery',
}
UNDER = '=-~^"'


def convert(path, pre=()):
    text = fix(open(path).read(), pre, os.path.basename(path))   # fixes inside tables go here
    rst = pypandoc.convert_text(text, 'rst', format='gfm+tex_math_dollars',
                                extra_args=['--columns=95', '--wrap=preserve'])
    rst = re.sub(r'^\.\. _[^:\n]+:\n\n', '', rst, flags=re.M)      # pandoc's heading labels

    def link(m):
        text, target = m.group(1).strip(), m.group(2)
        page = PAGE[target]
        return ':doc:`%s`' % page if text in (target, os.path.basename(target)) or \
            text.startswith('tests/vet_clean') else ':doc:`%s <%s>`' % (text, page)
    pat = re.compile(r'`([^`<\n]+)<([^>\s]+\.md)>`__')
    out = []
    for line in rst.split('\n'):
        if not line.startswith('|'):
            out.append(pat.sub(link, line))
            continue
        # grid-table row: keep every '|' in its column by taking the length change of a
        # replacement out of (or adding it to) the blanks before the cell's right border
        while True:
            m = pat.search(line)
            if not m:
                break
            new = link(m)
            d = len(new) - (m.end() - m.start())
            bar = line.index('|', m.end())
            if d > 0 and line[bar - d - 1:bar] != ' ' * (d + 1):
                sys.exit('sync_from_code: no room for %r in a table cell' % new)
            pad = line[m.end():bar - d] if d > 0 else line[m.end():bar] + ' ' * -d
            line = line[:m.start()] + new + pad + line[bar:]
        out.append(line)
    rst = '\n'.join(out)
    return rst


def headings(rst):
    """[(line index, level, title)] of the section titles of rst."""
    L = rst.split('\n')
    out = []
    for i in range(1, len(L)):
        u = L[i]
        if len(u) >= 3 and len(set(u)) == 1 and u[0] in UNDER and L[i - 1].strip() and \
                len(u) >= len(L[i - 1].rstrip()) and not L[i - 1].startswith(('+', '|')):
            out.append((i - 1, UNDER.index(u[0]), L[i - 1]))
    return out


def sections(rst):
    """{'_pre': text before the first level-1 section, title: text of that level-1 section}."""
    L = rst.split('\n')
    hs = [h for h in headings(rst) if h[1] == 1]
    first = headings(rst)[0]
    out = {'_pre': '\n'.join(L[first[0] + 2:hs[0][0] if hs else len(L)]).strip('\n')}
    for k, (i, _, t) in enumerate(hs):
        j = hs[k + 1][0] if k + 1 < len(hs) else len(L)
        out[re.sub(r'^\d+[a-z]?\.\s+', '', t)] = '\n'.join(L[i:j]).strip('\n')
    return out


def renumber(text, keep_blocks=False):
    """Strip '3.', '1.1' numbers from titles (keep '3a.' block labels if asked)."""
    L = text.split('\n')
    for i, _, t in headings(text):
        if keep_blocks and re.match(r'^\d+[a-z]\.\s', t):
            n = re.sub(r'^(\d+[a-z])\.\s+(.*)$', r'\2 (block \1)', t)
        else:
            n = re.sub(r'^(\d+[a-z]?\.|\d+(\.\d+)+)\s+', '', t)
        L[i], L[i + 1] = n, L[i + 1][0] * len(n)
    return '\n'.join(L)


def body(text):
    """A section without its title (for a page that is that one section)."""
    return text.split('\n', 2)[2].lstrip('\n')


def fix(text, subs, name):
    for old, new, *cnt in subs:
        n = text.count(old)
        if n != (cnt[0] if cnt else 1):
            sys.exit('sync_from_code: fix for %s matches %d times: %r' % (name, n, old))
        text = text.replace(old, new)
    return text


def figures(code):
    """Rows of docs/vet_clean/figures/FIGURES.md as dicts; copies the PNGs to source/figures/."""
    d = os.path.join(code, 'docs/vet_clean/figures')
    out = os.path.join(OUT, 'figures')
    shutil.rmtree(out, ignore_errors=True)
    if not os.path.exists(os.path.join(d, 'FIGURES.md')):
        return []
    os.makedirs(out)
    rows = []
    for line in open(os.path.join(d, 'FIGURES.md'), encoding='utf-8'):
        c = [x.strip() for x in line.strip().strip('|').replace('\\|', '\x00').split('|')]
        if len(c) == 4 and c[0].endswith('.png'):
            fig, _, tests, cap = (x.replace('\x00', '|') for x in c)
            shutil.copy(os.path.join(d, fig), out)
            rows.append({'fig': fig, 'tests': [t.strip() for t in tests.split(',')], 'cap': cap})
    return rows


def figure(r):
    """A figure directive; the caption's Markdown code spans and bars made rst-safe."""
    cap = re.sub(r'`([^`]+)`', r'``\1``', r['cap'].replace('|', '\\|'))
    return ('.. figure:: figures/%s\n   :alt: %s\n   :width: 100%%\n\n   %s'
            % (r['fig'], ', '.join(r['tests']), cap))


def with_figures(text, rows):
    """After each section whose 'Test:' / 'Tests:' paragraph names a test, its figures."""
    hs = headings(text)
    L = text.split('\n')
    cuts = [h[0] for h in hs if h[1] >= 2] + [len(L)]
    parts, done = ['\n'.join(L[:cuts[0]])], set()
    for a, b in zip(cuts[:-1], cuts[1:]):
        sec = '\n'.join(L[a:b]).rstrip('\n')
        m = re.search(r'^Tests?:(.*?)(?:\n\n|\Z)', sec, re.S | re.M)
        named = set(re.findall(r'``([A-Za-z0-9_\-]+)``', m.group(1))) if m else set()
        figs = [figure(r) for r in rows if named & set(r['tests']) and r['fig'] not in done]
        done.update(r['fig'] for r in rows if named & set(r['tests']))
        parts.append('\n\n'.join([sec] + figs) + '\n')
    return '\n\n'.join(parts)


def page(name, title, parts, src, intro=''):
    head = ('.. This page is generated by tools/sync_from_code.py from %s of the code\n'
            '   repository. Edit the Markdown there and re-run the script.\n\n' % src)
    body = '\n\n'.join(p for p in [intro] + parts if p)
    with open(os.path.join(OUT, name + '.rst'), 'w') as f:
        f.write(head + title + '\n' + '=' * len(title) + '\n\n' + body.rstrip() + '\n')
    print('wrote source/%s.rst' % name)


def performance(code):
    """The page of docs/vet_clean/PERFORMANCE.md; copies its figure and data files."""
    d = os.path.join(code, 'docs/vet_clean')
    if not os.path.exists(os.path.join(d, 'PERFORMANCE.md')):
        return
    out = os.path.join(OUT, 'performance')
    shutil.rmtree(out, ignore_errors=True)
    shutil.copytree(os.path.join(d, 'performance'), out, ignore=shutil.ignore_patterns('__pycache__'))
    rst = convert(os.path.join(d, 'PERFORMANCE.md')).split('\n', 2)[2].lstrip('\n')
    rst = re.sub(r'`([^`<\n]+)\s<(performance/[^>\s]+)>`__', r':download:`\1 <\2>`', rst)
    page('performance', 'Performance on 3-D wedges of stars', [renumber(rst)], 'docs/vet_clean/PERFORMANCE.md')


def main(code):
    D = os.path.join(code, 'docs/vet_clean')
    T = os.path.join(code, 'tests/vet_clean')
    rev = subprocess.run(['git', '-C', code, 'rev-parse', '--short=9', 'HEAD'],
                         stdout=subprocess.PIPE, universal_newlines=True).stdout.strip()
    md = {k: convert(os.path.join(D, k)) for k in
          ('QUICKSTART.md', 'BUILD.md', 'RUN.md', 'KEYS.md', 'OUTPUTS.md', 'SCHEME.md', 'STARS.md')}
    md['TESTS'] = convert(os.path.join(T, 'README.md'))
    md['NB'] = convert(os.path.join(T, 'notebooks/README.md'))

    q = md['QUICKSTART.md']
    q = fix(q, [
        ('(examples in section 3)', '(examples in :doc:`build`)'),
        ('Check any new GPU binary with section 4.', 'Check any new GPU binary with the check of\n:doc:`quickstart`.'),
        ('the host compiler is ``CC``:1', 'the host compiler is ``CC``: [#f1]_'),
        ('per\nMI300A.2', 'per\nMI300A. [#f2]_'),
        ('``build_star/src/athena`` (section 3)', '``build_star/src/athena`` (:doc:`build`)'),
        ('--------------\n\n1 Block 3c', '.. rubric:: Notes\n\n.. [#f1] Block 3c'),
        ('Sections 2, 3a, 4, 5 and 6 and the CPU start-up check of\nSTARS.md',
         'The download, block 3a, the check, the run by hand and the notebooks of\n'
         ':doc:`quickstart`, and the CPU start-up check of :doc:`stars`,'),
        ('the GPU quick suite of section 4', 'the GPU quick suite of :doc:`quickstart`'),
        ('\n2 With ROCm 7.2', '\n.. [#f2] With ROCm 7.2'),
    ], 'QUICKSTART.md')
    q = re.sub(r'\n(\.\. \[#f[12]\] )([^\n]*)((?:\n[^\n]+)*)',
               lambda m: '\n' + m.group(1) + m.group(2) + m.group(3).replace('\n', '\n   '), q)
    qs = sections(q)
    b = sections(md['BUILD.md'])
    notes = qs['Further reading'].split('.. rubric:: Notes', 1)[1]
    page('requirements', 'Requirements', [body(qs['What you need'])], 'docs/vet_clean/QUICKSTART.md')
    dl = fix(qs['Download'], [('git clone <repo-url> athenak',
                               'git clone https://github.com/jing-ze-ma/athenak.git athenak')], 'Download')
    page('download', 'Download', [body(dl)], 'docs/vet_clean/QUICKSTART.md',
         'This site documents release ``vet-clean-release`` (commit ``%s``).' % rev)
    page('build', 'Build', [re.sub(r'\n~{3,}\n', lambda m: m.group(0).replace('~', '-'),
                            body(renumber(qs['Build'], keep_blocks=True))),
                            renumber(b['Options that matter for this scheme']),
                            renumber(b['Build time']),
                            '.. rubric:: Notes' + notes],
         'docs/vet_clean/QUICKSTART.md and BUILD.md')
    page('quickstart', 'Quickstart', [renumber(qs[k]) for k in
         ('Check the build', 'Run a test problem by hand', 'Plots in Jupyter',
          '3-D stars in spherical-polar and cubed-sphere coordinates')],
         'docs/vet_clean/QUICKSTART.md',
         'Check a build, run the test suite, run a problem by hand and plot it. Build first\n'
         '(:doc:`build`); all commands run from the ``athenak/`` directory.')
    page('notes_specific_machines', 'Notes on specific machines',
         [renumber(b['NVIDIA GPUs (CUDA)']), renumber(b['AMD GPUs (HIP, MI300A)'])],
         'docs/vet_clean/BUILD.md',
         'Toolchains that are known to work (and one that is not), and run-time settings per\n'
         'machine. The build blocks themselves are on :doc:`build`.')

    r = sections(fix(md['RUN.md'], [
        ('(:doc:`outputs`, section 4.2)', '(:doc:`outputs`, "Other per-cycle lines")')], 'RUN.md'))
    page('running_the_code', 'Running the code', [renumber(r[k]) for k in
         ('A first run (CPU, one minute)', 'Production star runs', 'Checking a run',
          'Why is my run slow? (the time-step report)', 'GPU memory on spherical-polar wedges')],
         'docs/vet_clean/RUN.md')

    ks = sections(convert(os.path.join(D, 'KEYS.md'), [
        ('(RUN.md section 6)', '(Running the code: GPU memory)'),
        ('; RUN.md section 5)', '; Running the code: the time-step report)')]))
    t = sections(md['TESTS'])
    page('input_file', 'The input file', [ks['_pre'], renumber(ks['The restart rule']),
                                          renumber(t['The decks'])],
         'docs/vet_clean/KEYS.md and tests/vet_clean/README.md',
         'An input deck is a plain AthenaK ``.athinput`` file; the scheme reads the\n'
         '``<rad_vet>`` block (the old name ``<rad_m1>`` is accepted as an alias). Any key can be\n'
         'changed on the command line as ``block/key=value``.')
    page('keys', 'Keys reference', [renumber(v) for n, v in ks.items()
                                    if n not in ('_pre', 'The restart rule')],
         'docs/vet_clean/KEYS.md',
         'The keys a user sets, by topic. How keys combine on a restart:\n'
         ':doc:`input_file`.')

    tt = fix(md['TESTS'], [('``docs/vet_clean/BUILD.md``', ':doc:`notes_specific_machines`'),
                           ('see ``notebooks/README.md``', 'see :doc:`gallery`')], 'tests README')
    ts = sections(tt)
    o = convert(os.path.join(D, 'OUTPUTS.md'), [('`KEYS.md`', '[KEYS.md](KEYS.md)', 3)])
    o = o.split('\n', 2)[2].lstrip('\n')     # its own title; section numbers are kept (cited)
    page('outputs', 'Outputs', [o], 'docs/vet_clean/OUTPUTS.md')
    nb = sections(fix(md['NB'], [('# the CPU build of QUICKSTART.md 3a', '# the CPU build (block 3a)')],
                      'notebooks/README.md'))
    page('analysis', 'Analysis', [renumber(ts['Files']), renumber(ts['Notebooks']),
                                  renumber(nb['How to run'])],
         'tests/vet_clean/README.md and notebooks/README.md',
         'Python readers for the outputs (``tests/vet_clean/vett.py``, standard library + numpy)\n'
         'and the notebooks. How to check the energy and mass conservation of a run from its\n'
         'history file: :doc:`outputs`, section 3. Worked examples with plots: :doc:`gallery`.')

    s = sections(fix(md['SCHEME.md'], [
        ('(see its README for\nthe decks and the exact criteria)', '(see :doc:`tests` for\nthe decks and the exact criteria)'),
        ('(``tests/vet_clean/README.md``, "GPU builds")', '(:doc:`tests`, "GPU builds")'),
    ], 'SCHEME.md'))
    page('scheme', 'The VET scheme', [s['_pre'], renumber(s['The method in brief']),
                                      renumber(s['Code map']), renumber(s['How to cite'])],
         'docs/vet_clean/SCHEME.md')
    performance(code)
    figs = figures(code)
    tfigs = [r for r in figs if not r['tests'][0].startswith('star3d')]
    page('properties', 'Properties', [with_figures(body(s['Properties']), tfigs)],
         'docs/vet_clean/SCHEME.md',
         'What each property means, how the scheme achieves it, and the test that shows it\n'
         '(:doc:`tests`; worked notebooks in :doc:`gallery`).')

    page('tests', 'Tests', [ts['_pre']] + [renumber(ts[n]) for n in
                                           ('What the tests check', 'GPU builds', 'Notebooks')] +
         (['Plots\n-----\n\nThe key plot of each test, from its notebook (``docs/vet_clean/figures/``).']
          + [figure(r) for r in tfigs] if tfigs else []),
         'tests/vet_clean/README.md')
    st = sections(fix(md['STARS.md'], [
        ('``clean_init_tol = 2.0e-7``, see section 3.', '``clean_init_tol = 2.0e-7``, see "What to look at".'),
        (':doc:`quickstart` section 3', ':doc:`build`')], 'STARS.md'))
    page('stars', '3-D stars: spherical polar and cubed sphere',
         [st['_pre']] + [renumber(v) + ('\n\n' + '\n\n'.join(
             figure(r) for r in figs if r['tests'][0].startswith('star3d'))
             if n == 'What to look at' else '') for n, v in st.items() if n != '_pre'],
         'docs/vet_clean/STARS.md',
         'Step-by-step versions with the decks and the executed notebook: the ``star3d-sp`` and\n'
         '``star3d-cs`` tutorials of the :doc:`gallery`.')


if __name__ == '__main__':
    main(os.path.abspath(sys.argv[1]))
