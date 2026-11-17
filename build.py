"""Build the four-course portfolio hub. Run python build.py; no dependencies."""
from pathlib import Path
from html import escape as e
import json,re
R=Path(__file__).parent
BASE='https://iratt.github.io/portfolios/'
V=R/'assets/visuals';V.mkdir(exist_ok=True)
ink='#14323a';teal='#176b67';gold='#eab866';muted='#51646a'
def text(x,y,s,size=18,color=ink,weight='normal',anchor='start'):
 return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" font-weight="{weight}" text-anchor="{anchor}">{e(str(s))}</text>'
def rect(x,y,w,h,fill=teal):return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{fill}"/>'
def line(x,y,x2,y2,c=teal):return f'<path d="M{x} {y} L{x2} {y2}" fill="none" stroke="{c}" stroke-width="4" marker-end="url(#arrow)"/>'
def svg(name,title,subtitle,body):
 (V/(name+'.svg')).write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 420" role="img" aria-labelledby="title desc"><title id="title">{e(title)}</title><desc id="desc">{e(subtitle)}</desc><defs><marker id="arrow" markerWidth="7" markerHeight="7" refX="5" refY="3" orient="auto"><path d="M0 0 L6 3 L0 6" fill="{teal}"/></marker></defs><rect width="760" height="420" rx="14" fill="#edf1e9"/><g font-family="Arial,sans-serif">'+text(32,44,title,25,ink,'bold')+text(32,72,subtitle,15,muted)+body+'</g></svg>')
def steps(name,title,subtitle,items):
 body=''
 for i,(a,b) in enumerate(items):
  y=100+i*72
  body+=rect(32,y,44,44)+text(54,y+29,f'{i+1:02}',18,'white','bold','middle')+text(94,y+19,a,21,ink,'bold')+text(94,y+44,b,16,muted)
 svg(name,title,subtitle,body)
mods=json.loads((R/'data/modules.json').read_text())
assert len(mods)==24
body=text(32,111,'100%',19,teal,'bold')+text(32,339,'0%',15,muted)
for i in range(24):
 x=87+i*26
 body+=rect(x,123,17,207,teal if i<12 else '#388c86')+text(x+8,357,str(i+1),12,muted,anchor='middle')
body+=text(390,391,'Course modules 01–24 · final record',16,muted,anchor='middle')
svg('mit-marks','Full marks across all 24 modules','Final course record: 813 / 813 points across 144 graded activities.',body)
steps('mit-methods','Data in context. Decisions with value.','Program wrap-up: turn analytical techniques into better business decisions.', [('Understand','Visualize the data and examine its statistics.'),('Predict','Build predictive models; evaluate advanced methods.'),('Optimize','Choose actions within objectives and constraints.'),('Extend','Apply deep learning where the problem supports it.')])
body=''
for i,(label,val) in enumerate([('Product x1',115),('Product x2',0),('Product x3',0)]):
 y=115+i*72;body+=text(32,y+28,label,19)+rect(175,y,500,37,'#dce5dd')
 if val:body+=rect(175,y,500*val/115,37)
 body+=text(700,y+27,val,20,ink,'bold','end')
body+=text(32,371,'115 × 15 = 1,725 profit units in this submitted model',20,teal,'bold')
svg('mit-production','Production optimization: the selected mix','Module 09 · model extract · quantities in model units, not measured output.',body)
steps('bacnet-levels','Integration at four levels','A system must work across equipment, functions, applications and sites.', [('Device','Exchange values and commands with equipment.'),('Functional','Coordinate functions such as occupancy and HVAC.'),('Application','Connect maintenance, reporting and workflows.'),('Cloud','Bring context together across a portfolio of sites.')])
body=rect(32,126,265,132)+rect(463,126,265,132,ink)+text(164,162,'Controller',25,'white','bold','middle')+text(164,195,'DS-RP-A',24,gold,'bold','middle')+text(164,229,'Initiates ReadProperty',17,'white',anchor='middle')+text(595,162,'Thermostat',25,'white','bold','middle')+text(595,195,'DS-RP-B',24,gold,'bold','middle')+text(595,229,'Responds to ReadProperty',17,'white',anchor='middle')+line(305,162,451,162)+line(455,226,309,226)+text(380,143,'Request',16,teal,anchor='middle')+text(380,255,'Response',16,teal,anchor='middle')+text(32,322,'Complementary capabilities enable the exchange.',22,ink,'bold')+text(32,356,'Check the PICS, required services and point permissions together.',17,muted)
svg('bacnet-pair','Two sides of a BACnet exchange','Study-guide example: a client reads a property from a supporting device.',body)
body=text(32,122,'Individual reads',20)+rect(32,140,630,45)+text(680,171,'20',23,ink,'bold')+text(32,230,'Grouped read',20)+rect(32,248,63,45,gold)+text(113,279,'2',23,ink,'bold')+text(32,340,'Application messages per minute',20,ink,'bold')+text(32,373,'Assumes one grouped request and response can carry all ten points.',15,muted)
svg('bacnet-traffic','Communication workload matters','Illustration: ten points, read once per minute; request + response counted.',body)
steps('schneider-chain','Infrastructure supports a business service','Course synthesis: examine dependencies together.', [('Power','Supply, backup, distribution and rack delivery.'),('Cooling','Airflow, humidity and heat removal at the load.'),('Connectivity & protection','Cabling, physical access and fire protection.'),('Operations','Asset context, monitoring and recovery procedures.')])
body=rect(32,122,195,150,'#d2e6e4')+rect(284,122,192,150,ink)+rect(533,122,195,150,'#ecd7b4')+text(129,163,'Cold aisle',25,teal,'bold','middle')+text(129,200,'Rack inlet',18,ink,anchor='middle')+text(129,233,'Supply air',18,ink,anchor='middle')+text(380,164,'IT rack',25,'white','bold','middle')+text(380,200,'Front → back',18,'white',anchor='middle')+text(380,233,'Heat added',18,gold,anchor='middle')+text(631,163,'Hot aisle',25,ink,'bold','middle')+text(631,200,'Rack exhaust',18,ink,anchor='middle')+text(631,233,'Return air',18,ink,anchor='middle')+line(232,196,275,196)+line(482,196,526,196)+text(32,327,'Keep supply and return air separated.',23,ink,'bold')+text(32,365,'Control bypass and recirculation; check the conditions at rack inlets.',16,muted)
svg('schneider-airflow','Follow the air through the load','Conceptual cooling diagram redrawn from the course themes; not to scale.',body)
body=text(32,118,'MTBF 50,000 h',20)+rect(32,138,586,43)+text(637,168,'42.0',22,ink,'bold')+text(32,226,'MTBF 200,000 h',20)+rect(32,246,146.5,43,gold)+text(198,277,'10.5',22,ink,'bold')+text(32,336,'Expected unavailable minutes / year',20,ink,'bold')+text(32,369,'Assumptions: MTTR = 4 h; 8,760 h/year. A = MTBF / (MTBF + MTTR).',15,muted)
svg('schneider-availability','Reliability and recovery shape availability','Calculated illustration using the study reference’s MTBF examples.',body)
body=''
for i,(a,b) in enumerate([('Client 1','Managed hosting'),('Client 2','Data blocks / movers'),('Client 3','Cloud racks / network')]):
 x=32+i*245;body+=rect(x,118,225,100,teal if i!=1 else ink)+text(x+18,153,a,23,'white','bold')+text(x+18,190,b,16,'white')
body+=rect(32,240,470,61,'#dce5dd')+text(51,277,'Circulation + supporting infrastructure',20)+rect(521,240,207,61,'#ecd7b4')+text(539,277,'Expansion space',19)+text(32,350,'A client business update changes the supporting design.',21,ink,'bold')+text(32,383,'Spatial relationships are illustrative; this is not the original floor plan.',15,muted)
svg('cdcdp-zones','West Hall: organize around client needs','Source: IA final case-study presentation, layout and revised client scenario.',body)
body=rect(32,117,255,70,teal)+text(159,162,'Power pathway A',23,'white','bold','middle')+rect(32,250,255,70,ink)+text(159,295,'Power pathway B',23,'white','bold','middle')+rect(498,155,230,129,'#dce5dd')+text(613,201,'IT cabinet',25,ink,'bold','middle')+text(613,240,'A / B connections',18,ink,anchor='middle')+line(295,152,480,184)+line(295,285,480,254)+text(32,369,'Trace each path and reconcile it with the cabinet schedule.',20,ink,'bold')
svg('cdcdp-paths','Make supporting pathways visible','Schematic summary of the case-study A/B distribution layer; not a design rating.',body)
steps('cdcdp-layers','One design, coordinated layers','Final case-study presentation: spatial, technical and protection views.', [('Space & cooling','Client zones, cabinets, CRAH units and circulation.'),('Power','A/B distribution components and pathways.'),('Connectivity','A/B network cabling pathways.'),('Protection','Smoke detection, sprinklers, cameras and access.')])
captions={
 'mit':[('mit-marks','A consistent result','Every module achieved 100%. Source: final course record; the expandable record below retains the detail.'),('mit-methods','From understanding to action','A visual synthesis of the program wrap-up and five key takeaway areas.'),('mit-production','A model you can inspect','Module 09 production mix, redrawn from the published model extract. The objective value is 1,725 in the model’s units.')],
 'bacnet':[('bacnet-levels','Integration beyond a protocol label','Redrawn from the BACnet Basics study guide: integration has device, functional, application and cloud dimensions.'),('bacnet-pair','Capabilities must complement each other','The study-guide ReadProperty example pairs an initiating controller with a responding device.'),('bacnet-traffic','Group reads where the device supports them','Study-guide illustration: ten individual reads produce 20 messages; one grouped exchange produces two. Counts exclude other traffic and protocol overhead.')],
 'schneider':[('schneider-chain','Think in service dependencies','A diagram synthesizing the fourteen-module study reference: availability depends on the supporting systems and operations.'),('schneider-airflow','Make the airflow path legible','A conceptual redraw of course cooling themes. The diagram illustrates the air path, not a measured or commissioned installation.'),('schneider-availability','Restoration time belongs in the calculation','Study-reference reliability examples with an explicitly assumed four-hour repair time. Calculated illustration, not observed facility performance.')],
 'cdcdp':[('cdcdp-zones','Plan for different clients and change','Redrawn summary of the IA final case-study layout slides and subsequent business update. This zoning diagram is not to scale.'),('cdcdp-paths','Trace A and B independently','Conceptual redraw of the case-study distribution layer. No Tier classification or compliance conclusion is implied.'),('cdcdp-layers','Coordinate the design layers','Visual synthesis of the IA slides covering layout, power, network, detection, suppression and security.')]
}
css='''\n.visuals{padding:52px 0;border-top:1px solid #cdd5ce}.visuals>h2{font:38px Georgia,serif;margin:10px 0 26px}.visual-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:24px}.visual-grid figure{margin:0;border:1px solid #cdd5ce;border-radius:12px;overflow:hidden;background:#fffefa}.visual-grid figure:first-child{grid-column:1/-1;display:grid;grid-template-columns:1.65fr 1fr;align-items:center}.visual-grid img{display:block;width:100%;height:auto}.visual-grid figcaption{padding:23px;font-size:14px;line-height:1.65;color:#51646a}.visual-grid figcaption strong{display:block;color:#14323a;font:25px Georgia,serif;margin-bottom:10px}.visual-grid a{display:block;font-size:12px;margin-top:12px;color:#176b67}.course-thumb{width:100%;height:auto;border-radius:7px;margin:20px 0 0}.visuals .eyebrow{font:700 11px Arial,sans-serif;letter-spacing:1.8px;color:#176b67}.visuals{scroll-margin-top:100px}@media(max-width:700px){.visual-grid,.visual-grid figure:first-child{display:block}.visual-grid figure{margin-bottom:22px}.visuals>h2{font-size:31px}}'''
(R/'assets/visuals.css').write_text(css)
def gallery(slug):
 return '<section class="visuals" id="visual-learning"><span class="eyebrow">LEARNING, MADE VISIBLE</span><h2>Three views into the work.</h2><div class="visual-grid">'+''.join(f'<figure><img src="../assets/visuals/{n}.svg" alt="{e(t)}. {e(c)}" width="760" height="420" loading="lazy"><figcaption><strong>{e(t)}</strong>{e(c)}<a href="../assets/visuals/{n}.svg" target="_blank" rel="noopener">Open full-size diagram ↗</a></figcaption></figure>' for n,t,c in captions[slug])+'</div></section>'
mapping={'index.html':'mit/','portfolio.html':'','bacnet.html':'bacnet/','schneider.html':'schneider/','cdcdp.html':'cdcdp/'}
for source,dest in mapping.items():
 s=(R/'source'/source).read_text();prefix='../' if dest else ''
 s=s.replace('https://iratt.github.io/MIT-AI-ML/','https://iratt.github.io/portfolios/')
 for old,new in mapping.items():s=s.replace('https://iratt.github.io/portfolios/'+old,BASE+new)
 s=re.sub(r'((?:href|src)=")assets/',r'\1'+prefix+'assets/',s)
 s=re.sub(r'(href=")evidence/',r'\1'+prefix+'evidence/',s)
 for old,new in mapping.items():s=s.replace('href="'+old,'href="'+prefix+new)
 # Empty root href is explicit so navigation never reloads the current course.
 s=s.replace('href=""','href="./"')
 s=s.replace('</head>','<link rel="stylesheet" href="'+prefix+'assets/visuals.css"></head>')
 if dest:
  slug=dest[:-1]
  if slug=='mit':s=s.replace('<section class="section projects-section" id="projects">','<div class="wrap">'+gallery(slug)+'</div><section class="section projects-section" id="projects">')
  else:s=s.replace('<section class="section work">',gallery(slug)+'<section class="section work">')
  assert 'id="visual-learning"' in s,slug
  s=s.replace('https://github.com/IRATT/MIT-AI-ML','https://github.com/IRATT/portfolios')
 else:
  for slug,n in [('mit','mit-marks'),('bacnet','bacnet-pair'),('schneider','schneider-airflow'),('cdcdp','cdcdp-zones')]:
   pattern=r'(<a class="coursecard [^"]+" href="'+slug+r'/">.*?)(<div class="cardlink">)'
   s=re.sub(pattern,lambda m:m.group(1)+'<img class="course-thumb" src="assets/visuals/'+n+'.svg" alt="Visual preview of this course portfolio" width="760" height="420" loading="lazy">'+m.group(2),s)
 p=R/dest/'index.html';p.parent.mkdir(exist_ok=True);p.write_text(s)
(R/'.nojekyll').write_text('')
(R/'README.md').write_text('''# Ian Alleyne · Portfolios

[Open the portfolio hub](https://iratt.github.io/portfolios/)

- [MIT xPRO · Advanced Analytics with AI, ML, and Data Science](https://iratt.github.io/portfolios/mit/) — six months, 24 modules, 100%.
- [BACnet Basics](https://iratt.github.io/portfolios/bacnet/)
- [Schneider Electric · Data Center Foundations](https://iratt.github.io/portfolios/schneider/)
- [CNet / Uptime Education · CDCDP](https://iratt.github.io/portfolios/cdcdp/)

Each course is a continuous page with a collapsed course record and three source-based charts or diagrams. Figure captions distinguish final records, model results, calculations and conceptual redraws. These are independent learner portfolios; provider materials retain their original attribution. Original private certificate PDFs and course manuals are not included.

## Maintenance

Run `python build.py` to regenerate pages and diagrams from the reviewed source pages in `source/`. Serve the repository root as a static site. GitHub Pages uses the root of `main`.
''')
print('Built hub, four course pages and twelve visuals.')
