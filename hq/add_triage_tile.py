import sys,re
p=sys.argv[1]; s=open(p).read()
css='''
  /* Outlook Triage tile: mini version of the localhost:3000 app (deep purple, chip-tagged rows) */
  .tile.triage {
    background: #1a0f24;
    border: 1px solid #3a2550;
    flex-direction: column;
    align-items: stretch;
    justify-content: center;
    gap: 0.5rem;
    padding: 1.4rem 1.6rem;
    font-family: -apple-system, system-ui, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
  }
  .triage-title {
    color: #f8fafc; font-weight: 700; font-size: 1.45rem; letter-spacing: -0.01em;
    margin-bottom: 0.35rem; transition: transform 0.22s ease; transform-origin: left center;
  }
  .tile.triage:hover .triage-title { transform: scale(1.05); }
  .triage-row {
    display: flex; align-items: center; gap: 0.5rem;
    padding: 0.4rem 0.55rem; border-radius: 4px; background: #24163a;
  }
  .triage-row:first-of-type { outline: 1.5px solid #e8742c; outline-offset: -1.5px; }
  .triage-chip { width: 2.4rem; height: 0.55rem; border-radius: 2px; flex-shrink: 0; }
  .triage-line { height: 0.4rem; border-radius: 2px; background: rgba(248,250,252,0.55); }
'''
s=s.replace('\n  @media (prefers-reduced-motion: reduce) {', css+'\n  @media (prefers-reduced-motion: reduce) {',1)
s=s.replace('.tile, .tile img, .tile-name { transition: none; }','.tile, .tile img, .tile-name, .triage-title { transition: none; }',1)
tile='''
  <!-- Outlook Triage: local app, only works while it's running on localhost:3000 -->
  <a class="tile triage" title="Outlook Triage" href="http://localhost:3000" target="_blank">
    <span class="triage-title">Outlook Triage</span>
    <span class="triage-row"><span class="triage-chip" style="background:#c0392b"></span><span class="triage-line" style="width:70%"></span></span>
    <span class="triage-row"><span class="triage-chip" style="background:#e8622c"></span><span class="triage-line" style="width:52%"></span></span>
    <span class="triage-row"><span class="triage-chip" style="background:#e8622c"></span><span class="triage-line" style="width:62%"></span></span>
  </a>
'''
anchor='''    <span class="tile-name" style="font-family:Menlo, monospace">&gt;_</span>
  </a>
'''
assert anchor in s and 'tile triage' not in s
s=s.replace(anchor,anchor+tile,1)
open(p,'w').write(s)
print("patched")
