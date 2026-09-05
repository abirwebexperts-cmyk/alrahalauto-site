# Models (generate /models/<slug>/ and /services/<service>/<model>/ pages)
# Image: assets/img/models/<slug>.jpg (1200x1500 portrait recommended)
MODELS = [
 dict(slug="range-rover-vogue", name="Range Rover (Vogue)", short="L322, L405, L460", years="2002 – present",
  engines="3.0 TDV6/SDV6, 4.4 TDV8/SDV8, 5.0 V8 Supercharged, 3.0 Ingenium, P400e PHEV",
  intro="The flagship Range Rover is the reason our workshop exists. From the L322 with its BMW-derived electronics to the aluminium L405 and the current L460, we have serviced and repaired every generation of the full-size Range Rover.",
  issues=["Air suspension compressor and strut leaks","Timing chain wear on 3.0 V6 diesel and 5.0 V8","Coolant crossover pipe leaks on the V8","Battery drain from modules not sleeping","Tailgate and sunroof drainage faults"]),
 dict(slug="range-rover-sport", name="Range Rover Sport", short="L320, L494, L461", years="2005 – present",
  engines="3.0 TDV6/SDV6, 5.0 V8 Supercharged, 3.0 Ingenium P400, SVR 5.0",
  intro="The Range Rover Sport is driven harder than any other Land Rover, and it shows. Supercharger bearings, brake wear and air suspension on the SVR and V8 models are our daily work, alongside the diesel V6 family's timing chains.",
  issues=["Supercharger nose bearing whine on 5.0 V8","Front air strut and valve block leaks","Brake disc warping under hard use","ZF gearbox mechatronic faults","Rear differential and locking diff faults"]),
 dict(slug="range-rover-velar", name="Range Rover Velar", short="L560", years="2017 – present",
  engines="2.0 Ingenium P250/P300 petrol, 2.0 D180/D240 diesel, 3.0 P400 MHEV",
  intro="The Velar brought Ingenium engines, twin-screen Touch Pro Duo and 48V mild hybrid technology to the range. Its electronics are sophisticated and its Ingenium engines need precise oil care. We know both intimately.",
  issues=["Touch Pro Duo screen freezing","Ingenium timing chain and oil dilution on diesels","48V mild hybrid battery faults","Door handle deployment failures","Coolant leaks from the auxiliary pump"]),
 dict(slug="range-rover-evoque", name="Range Rover Evoque", short="L538, L551", years="2011 – present",
  engines="2.0 Si4 petrol, 2.2 SD4 diesel, 2.0 Ingenium petrol and diesel, P300e PHEV",
  intro="The Evoque is the most popular Range Rover in the region, and its compact size hides genuinely complex mechanicals. From the Haldex all-wheel-drive unit to the nine-speed automatic on later cars, we service every version.",
  issues=["Haldex all-wheel-drive pump and filter","Nine-speed ZF gearbox shift quality","Turbocharger and boost pipe faults","Rear tailgate wiring failure","Panoramic roof rattles and leaks"]),
 dict(slug="land-rover-defender", name="Land Rover Defender", short="L663 & classic", years="1983 – present",
  engines="2.0 Ingenium, 3.0 Ingenium P400 MHEV, 5.0 V8, 3.0 D300 diesel, classic TD5 & Puma",
  intro="Whether it is a classic 110 or the new L663 Defender, this is the vehicle that defines the brand. We look after both, from TD5 injector looms to the very latest D300 mild hybrid and the P525 V8.",
  issues=["Air suspension on L663 after off-road use","Ingenium oil dilution on short journeys","Classic TD5 injector harness oil contamination","Pivi Pro software issues","Coolant leaks on new Defender auxiliary pumps"]),
 dict(slug="land-rover-discovery", name="Land Rover Discovery", short="D3, D4, D5", years="2004 – present",
  engines="2.7 TDV6, 3.0 TDV6/SDV6, 5.0 V8, 3.0 Ingenium D300, 2.0 Ingenium",
  intro="The Discovery is the family workhorse, and Discovery 3 and 4 owners know its weak points well. Air suspension, timing chains and crankshaft concerns on the 2.7 and 3.0 diesels are our specialities.",
  issues=["Front air suspension and compressor on D3/D4","Timing chain stretch on 3.0 TDV6/SDV6","Crankshaft failure on early 3.0 diesels","Lower control arm and bush wear","Parking brake actuator failure on D3/D4"]),
]

# Brands. Image: assets/img/brands/<slug>.jpg (1600x900)
BRANDS = [
 dict(slug="range-rover", name="Range Rover", primary=True,
  intro="Range Rover is our home ground. Our founder trained on Range Rovers, our diagnostic equipment is Land Rover's own, and our parts stock is built around the Vogue, Sport, Velar and Evoque. We carry out engine rebuilds, air suspension, gearboxes, electronics and body work for every generation.",
  models=["range-rover-vogue","range-rover-sport","range-rover-velar","range-rover-evoque"]),
 dict(slug="land-rover", name="Land Rover", primary=True,
  intro="Defender, Discovery and Discovery Sport share their engineering DNA with the Range Rover family, and we service them with the same dealer-level tools and genuine parts. From classic TD5 Defenders to the new L663, no Land Rover is unfamiliar here.",
  models=["land-rover-defender","land-rover-discovery"]),
 dict(slug="bmw", name="BMW", primary=False,
  intro="Our BMW bay handles the full range from 3 Series to X7 and M models. ISTA diagnostics, N-series and B-series engine repairs, ZF gearbox services, timing chain replacements and the notorious oil filter housing and VANOS faults are all everyday work for our technicians.",
  models=[]),
 dict(slug="mercedes-benz", name="Mercedes-Benz", primary=False,
  intro="From the C-Class to the G-Class, we service Mercedes-Benz with XENTRY diagnostics and genuine parts. Airmatic suspension, 7G and 9G-Tronic gearbox services, balance shaft and timing chain repairs, and SBC brake systems are within our expertise.",
  models=[]),
 dict(slug="audi", name="Audi", primary=False,
  intro="Audi's quattro and S-tronic technology requires specialist knowledge. We service the A4 to the Q8, RS models included, using ODIS diagnostics for TFSI oil consumption fixes, timing chain tensioner updates, DSG mechatronic repair and air suspension on the Q7 and A8.",
  models=[]),
 dict(slug="porsche", name="Porsche", primary=False,
  intro="Cayenne, Macan and Panamera owners trust us for PDK services, air suspension, coolant pipe upgrades and bore scoring inspections. We use PIWIS diagnostics and follow Porsche procedures for every job.",
  models=[]),
 dict(slug="jaguar", name="Jaguar", primary=False,
  intro="Sharing engines and electronics with Land Rover, Jaguar F-Pace, XF, XE and F-Type models fit naturally into our workshop. Ingenium and supercharged V8 engine work, InControl repairs and suspension are all handled with the same tools we use on Range Rovers.",
  models=[]),
 dict(slug="bentley-rolls-royce", name="Bentley & Rolls-Royce", primary=False,
  intro="For Bentayga, Continental GT, Cullinan and Ghost owners we offer discreet, precise servicing and repair with the correct diagnostic platforms and factory procedures, at a fraction of dealership pricing.",
  models=[]),
]

# Blog posts. Image: assets/img/blog/<slug>.jpg (1600x900)
POSTS = [
 dict(slug="range-rover-air-suspension-problems-uae", title="Why Range Rover Air Suspension Fails in the UAE (and How to Prevent It)", date="2026-08-28", cat="Air Suspension", read=6,
  excerpt="Heat, sand and short trips are a brutal combination for air suspension. Here is what actually fails, in what order, and the habits that add years to the system.",
  body="""<p>Ask any Range Rover owner in the Gulf what they worry about most and the answer is usually the same: the car sinking overnight. Air suspension has a reputation for fragility, but the truth is more specific. The system fails in predictable ways, in a predictable order, and most of those failures are preventable.</p>
<h2>The four components that fail first</h2>
<p>The rubber air springs are the first casualty. Ultraviolet light and 50-degree ambient temperatures harden the rubber, and the constant flexing of a car that is driven daily opens tiny cracks near the fold. The compressor is next. It is designed to run briefly at start-up and after height changes, but once a spring starts leaking it runs continuously to compensate, overheats and wears its piston seal. The dryer inside the compressor then saturates, sending moisture into the valve block, where corrosion causes the third failure. Height sensors, exposed to sand and stone strikes, are the fourth.</p>
<h2>Why sand matters more than you think</h2>
<p>Fine desert sand finds its way into the compressor's intake filter and into the folds of the air spring. Inside the fold it acts like sandpaper on every bump. Owners who drive on the beach or dunes regularly should have the springs washed out and the compressor filter replaced far more often than the service schedule suggests.</p>
<h2>Habits that extend the life of the system</h2>
<ul><li>Park in shade wherever possible. It is the single most effective step.</li><li>Do not leave the vehicle in access height for long periods; the springs are compressed and the rubber folds harder.</li><li>Have the system pressure-tested every year. A leak caught early is a strut replacement. A leak ignored is a strut, compressor and valve block.</li><li>Replace the compressor dryer at the first sign of a slow rise.</li></ul>
<h2>What a proper repair looks like</h2>
<p>A good workshop will never replace a compressor without first proving the springs and lines are tight. At Al Rahal we pressurise the system, soap-test every joint and read the compressor duty cycle from the module before quoting. If you are told you need a whole new system, ask for the leak test results first.</p>
<p>If your Range Rover is sitting low this morning, send us a photo on WhatsApp and we will tell you what to expect before you drive in.</p>"""),
 dict(slug="tdv6-timing-chain-warning-signs", title="TDV6 and SDV6 Timing Chain: The Warning Signs Every Owner Should Know", date="2026-08-14", cat="Engine", read=7,
  excerpt="A two-second rattle on cold start is the sound of a timing chain asking for help. Here is how the fault develops and when it becomes urgent.",
  body="""<p>The 3.0-litre V6 diesel powered the Discovery 4, Range Rover Sport and full-size Range Rover for more than a decade. It is smooth, torquey and, with the right care, capable of very high mileages. It also has one weakness that every owner should understand: the timing chain.</p>
<h2>How the wear develops</h2>
<p>The chain itself rarely snaps. What happens is gradual elongation as the pins and bushes wear, combined with softening of the hydraulic tensioner. As the chain lengthens, the tensioner extends further to take up slack until it reaches its limit. At that point the chain is loose at every cold start until oil pressure builds, and the rattle you hear is the chain slapping against its guides.</p>
<h2>The sound to listen for</h2>
<p>Start the engine after it has stood overnight and listen from the front, driver's side. A metallic rattle lasting one to three seconds that then disappears is the classic symptom. As wear progresses the noise lasts longer and can appear on hot restarts. In the final stage the engine may set camshaft correlation fault codes and run roughly at idle.</p>
<h2>Why oil quality is the whole story</h2>
<p>Chain wear on this engine correlates almost perfectly with oil change discipline. Extended intervals, incorrect specification oil and short journeys that never let the oil reach temperature all accelerate wear. Our recommendation for the Gulf is an oil and filter change every 8,000 km with the correct low-SAPS oil, regardless of what the service indicator says.</p>
<h2>When to act</h2>
<p>If you hear the rattle, book a diagnostic check. We can measure chain stretch from live camshaft timing data without dismantling anything. If stretch is confirmed, replacing the chain, guides and tensioners costs a fraction of an engine and returns the car to silent running. Leaving it risks the chain jumping timing, which bends valves and usually means a rebuild.</p>"""),
 dict(slug="range-rover-service-cost-sharjah", title="How Much Does Range Rover Servicing Really Cost in Sharjah?", date="2026-07-30", cat="Servicing", read=5,
  excerpt="An honest breakdown of what goes into a service, why dealer prices are what they are, and where a specialist saves you money without cutting corners.",
  body="""<p>Owners are often surprised by dealer service quotes, and equally surprised by cheap garages offering an 'oil change' for the price of a lunch. Neither tells the full story. Here is what a proper Range Rover service actually involves and what drives the cost.</p>
<h2>What is in a service</h2>
<p>A minor service includes engine oil to Land Rover specification, a genuine oil filter, a diagnostic scan, a software check and a full inspection. A major service adds air, cabin and fuel filters, brake fluid, and often spark plugs or the diesel water separator. The oil alone is a significant cost: a 5.0 V8 takes over eight litres of a specific synthetic grade.</p>
<h2>Where dealer prices come from</h2>
<p>Dealer labour rates cover showroom overheads, and their pricing structures are set centrally. The work itself is not necessarily better; the technicians at a good specialist are frequently former dealer staff using the same diagnostic platforms.</p>
<h2>Where a specialist saves you money</h2>
<ul><li>Lower labour rates without lower standards.</li><li>Genuine parts sourced at trade prices, or high-quality OE-equivalent where it makes sense.</li><li>Honest advice on what can wait. A dealer service advisor works to targets; we work to keep you coming back for a decade.</li><li>Interim oil changes priced sensibly, so you can protect the engine without a full service every time.</li></ul>
<h2>Where you should never save money</h2>
<p>Oil specification, filter quality and the diagnostic scan. A garage that cannot read your service data cannot reset the schedule correctly or check for software updates, and a wrong oil grade quietly shortens the life of the timing chain and turbo.</p>
<p>For a clear, fixed price for your model, message us on WhatsApp with the registration and current mileage.</p>"""),
 dict(slug="range-rover-gearbox-fluid-lifetime-myth", title="The 'Lifetime' Gearbox Fluid Myth", date="2026-07-16", cat="Gearbox", read=5,
  excerpt="ZF, the company that builds the gearbox, recommends a fluid change. Here is why the phrase 'sealed for life' costs owners so much money.",
  body="""<p>The ZF eight-speed automatic in your Range Rover is one of the finest transmissions ever fitted to a road car. It is also a victim of a marketing phrase. 'Sealed for life' was never meant to mean the fluid lasts forever; it meant the gearbox does not need topping up between services. Somewhere along the way that became 'never change it'.</p>
<h2>What ZF actually says</h2>
<p>ZF's own guidance recommends an oil and filter change between 80,000 and 120,000 km depending on use. In extreme heat, stop-start traffic and towing, the lower figure applies. The fluid degrades with heat cycles, loses its friction modifiers and carries fine clutch material through the valve body.</p>
<h2>The symptoms of tired fluid</h2>
<p>Harsh downshifts when slowing to a stop, a delay when selecting drive from park, shuddering at low speed and a general loss of smoothness. Many owners assume this is 'just how it is now'. It is not.</p>
<h2>Why the method matters</h2>
<p>A gearbox fluid change is not a drain and refill. The fluid must be set at a precise temperature, the level checked through the overflow plug, and the adaptations reset so the transmission relearns its shift points. Done wrong, it can feel worse than before. Done right, it feels like a new car.</p>
<h2>Our recommendation</h2>
<p>Change the fluid and filter every 60,000 km in Gulf conditions. It costs far less than a valve body, and a fraction of a rebuild.</p>"""),
 dict(slug="buying-used-range-rover-checklist", title="Buying a Used Range Rover: The 12-Point Checklist We Use", date="2026-07-02", cat="Buying Guide", read=8,
  excerpt="Before you fall in love with the paint colour, run through the checks our technicians perform on every pre-purchase inspection.",
  body="""<p>A used Range Rover can be one of the best value luxury purchases available, or one of the most expensive mistakes. The difference is almost always in the history and the condition of a handful of known components. Here is the checklist we work through.</p>
<h2>Before you visit</h2>
<ol><li>Ask for the full service history and check the intervals. Gaps over 20,000 km are a red flag.</li><li>Ask who serviced it. Dealer or specialist history is worth paying for.</li><li>Check the registration for accident records and outstanding finance.</li></ol>
<h2>At the car, engine off</h2>
<ol start="4"><li>Look at the ride height on all four corners. A low corner means an air spring leak.</li><li>Check the oil. Milky residue under the filler cap or coolant in the expansion tank suggests head problems.</li><li>Inspect the tyres for uneven inner-edge wear, which points to alignment or suspension bush issues.</li></ol>
<h2>Cold start</h2>
<ol start="7"><li>Listen for a timing chain rattle in the first three seconds.</li><li>Watch for smoke. Blue is oil, white that persists is coolant.</li><li>Check every warning light extinguishes.</li></ol>
<h2>On the road</h2>
<ol start="10"><li>Feel for gearbox harshness, particularly on downshifts to a stop.</li><li>Listen for driveline whine that changes with speed.</li><li>Test every electrical function: windows, seats, tailgate, cameras, climate.</li></ol>
<h2>Then get it on a lift</h2>
<p>None of this replaces a professional inspection with a diagnostic scan. Stored fault history tells a story the seller may not, and two hours on our ramp can reveal underbody damage, leaks and previous repairs. Our pre-purchase inspection includes a written report you can use to negotiate.</p>"""),
 dict(slug="5-0-v8-supercharged-known-issues", title="Range Rover 5.0 V8 Supercharged: Known Issues and How We Fix Them", date="2026-06-18", cat="Engine", read=7,
  excerpt="The supercharged V8 is glorious to drive and demanding to own. These are the five faults we see most, and the permanent fixes for each.",
  body="""<p>The 5.0-litre supercharged V8 turns a two-and-a-half tonne Range Rover into a sports car. Owners adore it. Technicians respect it. It has a set of well-documented weaknesses that, once addressed properly, leave you with an engine that runs beautifully for years.</p>
<h2>1. Supercharger nose bearing</h2>
<p>A whine that rises with engine speed, most noticeable at idle with the bonnet open, is the supercharger's front coupling and bearing wearing out. The fix is a nose cone rebuild with an upgraded coupling. It is not a supercharger replacement.</p>
<h2>2. Coolant crossover pipes</h2>
<p>The plastic pipes running beneath the supercharger become brittle in heat and crack. The symptoms are a coolant smell and a level that drops slowly. Access requires supercharger removal, so we fit aluminium replacements that will never fail again.</p>
<h2>3. Timing chain tensioners</h2>
<p>Early engines had tensioners that could lose pressure on cold start. The updated tensioners and guides cure a rattle that, left alone, can cost the engine.</p>
<h2>4. Water pump</h2>
<p>A weeping water pump is normal wear at 100,000 km. We replace it with the thermostat and belt at the same time to avoid repeating the labour.</p>
<h2>5. Oil consumption and PCV</h2>
<p>A clogged crankcase ventilation system raises oil consumption and can push oil past seals. A PCV service is cheap and often transforms consumption.</p>
<p>Every one of these repairs is carried out in-house with genuine or upgraded parts. If your V8 is showing any of these symptoms, message us for a diagnosis before summer arrives.</p>"""),
 dict(slug="evoque-haldex-service-guide", title="Evoque Owners: Your Haldex Unit Needs a Service", date="2026-06-04", cat="Drivetrain", read=4,
  excerpt="The all-wheel-drive coupling on the Evoque has a filter and oil that most garages ignore. Here is why that leads to a very expensive repair.",
  body="""<p>The Range Rover Evoque sends power to the rear wheels through a Haldex coupling, an electronically controlled clutch pack that engages when the front wheels slip. It is compact, clever and almost always neglected.</p>
<h2>What goes wrong</h2>
<p>The Haldex unit has its own oil and a small filter screen. Over time, clutch material clogs the filter, the pump starves and the unit either stops engaging or sets a fault. Many owners only discover the problem when a warning appears or the rear wheels no longer drive on a wet road.</p>
<h2>The service that prevents it</h2>
<p>An oil change and filter clean every 40,000 km keeps the pump happy. It takes under an hour and costs very little. Skipping it leads to pump failure and, eventually, a complete coupling replacement at many times the cost.</p>
<h2>Signs the unit is already suffering</h2>
<ul><li>All-wheel-drive fault or 'traction reduced' message</li><li>Front wheels spinning on a wet or sandy surface while the rears do nothing</li><li>Whining from the rear of the vehicle</li></ul>
<p>Not sure if yours has been done? Send us your mileage on WhatsApp and we will tell you whether it is due.</p>"""),
 dict(slug="summer-preparation-range-rover", title="Preparing Your Range Rover for the Gulf Summer", date="2026-05-20", cat="Servicing", read=5,
  excerpt="Ten things to check before the temperature passes 45 degrees, from coolant condition to the battery you did not know you had.",
  body="""<p>Summer in the Gulf is a stress test for every vehicle, and a Range Rover's complexity means there are more things to check than on a simple car. We recommend this inspection every May.</p>
<h2>Cooling system</h2>
<p>Have the coolant tested for strength and the system pressure-tested. Check the radiator fins for sand build-up and the electric fan operation. A weak system that copes in March will fail in July.</p>
<h2>Air conditioning</h2>
<p>A performance check measures vent temperature against ambient. Evaporator cleaning removes the musty smell and improves airflow, and a new cabin filter is essential after the spring dust storms.</p>
<h2>Batteries</h2>
<p>Heat shortens battery life more than cold. Both the main and auxiliary batteries should be load-tested. A battery over two years old is living on borrowed time.</p>
<h2>Tyres</h2>
<p>Check pressures cold, inspect for sidewall cracking and confirm the date codes. Tyres over five years old harden and lose grip regardless of tread depth.</p>
<h2>Oil</h2>
<p>If your last oil change was more than 8,000 km ago, change it now. Thin, degraded oil and extreme heat are the enemies of the timing chain and turbo.</p>
<h2>Air suspension</h2>
<p>A quick pressure-hold test identifies early leaks before the compressor is forced to work overtime in the heat.</p>
<p>Our summer preparation package covers all of the above in a single visit. Book on WhatsApp.</p>"""),
 dict(slug="range-rover-battery-drain-causes", title="Range Rover Battery Drain: The Seven Usual Suspects", date="2026-05-06", cat="Electrical", read=6,
  excerpt="A flat battery after a weekend is almost never the battery's fault. Here are the modules and habits that keep your Range Rover awake at night.",
  body="""<p>Your Range Rover should be able to sit for two weeks and start first time. When it cannot, the cause is a parasitic drain: something is drawing current after the vehicle should have gone to sleep. Replacing the battery treats the symptom for a few months and then the problem returns.</p>
<h2>The usual suspects</h2>
<ol><li><strong>Infotainment module</strong> failing to power down, common on early InControl Touch systems.</li><li><strong>Telematics unit</strong> repeatedly trying to connect to a server.</li><li><strong>Tailgate or door latch</strong> not registering closed, keeping the body module awake.</li><li><strong>Aftermarket accessories</strong>: dash cameras, trackers and audio wired to permanent live.</li><li><strong>Water ingress</strong> into a module, usually through a blocked sunroof drain.</li><li><strong>A key fob left inside the vehicle</strong>, which keeps the keyless system polling.</li><li><strong>A failing auxiliary battery</strong> dragging down the main battery through the interconnect.</li></ol>
<h2>How we find it</h2>
<p>We measure current draw over a full sleep cycle with the bonnet latch tricked closed, then pull fuses one by one while watching the meter. It takes patience, not guesswork, and the result is a fix that lasts.</p>
<p>If your battery has been replaced twice and the problem persists, it was never the battery.</p>"""),
 dict(slug="ingenium-engine-oil-dilution-explained", title="Ingenium Diesel Oil Dilution Explained", date="2026-04-22", cat="Engine", read=5,
  excerpt="If your oil level is rising rather than falling, your Ingenium diesel is telling you something important about how it is being driven.",
  body="""<p>Owners of Ingenium-engined Velars, Evoques and Defenders sometimes notice the oil level creeping upward between services. It seems impossible. The explanation is oil dilution, and understanding it will protect your engine.</p>
<h2>What is happening</h2>
<p>To regenerate the diesel particulate filter, the engine injects extra fuel late in the combustion cycle to raise exhaust temperature. Some of that fuel washes past the piston rings into the sump. On a long motorway run, the heat evaporates it off again. On short urban journeys the regeneration is interrupted, the fuel accumulates, and the oil thins.</p>
<h2>Why it matters</h2>
<p>Diluted oil loses its film strength. The timing chain, camshaft and turbocharger are the first components to suffer, and the Ingenium timing chain in particular is sensitive to poor lubrication.</p>
<h2>What to do</h2>
<ul><li>Once a week, drive for 30 minutes at motorway speed to complete a regeneration.</li><li>Change the oil every 8,000 km if most of your driving is urban.</li><li>Never ignore an oil level above the maximum mark. Have it changed.</li><li>If a DPF warning appears, book a forced regeneration promptly.</li></ul>
<p>If your driving is almost entirely short trips, we can advise whether a diesel is the right choice for your next vehicle.</p>"""),
 dict(slug="brake-judder-range-rover-sport", title="Brake Judder on the Range Rover Sport: Causes and the Right Fix", date="2026-04-08", cat="Brakes", read=4,
  excerpt="Vibration through the steering wheel when braking from speed has three possible causes. Only one of them is warped discs.",
  body="""<p>Brake judder is one of the most common complaints on the Range Rover Sport, and the standard answer, new discs and pads, does not always cure it. Here is what actually causes it and how we diagnose the right fix.</p>
<h2>Cause one: disc thickness variation</h2>
<p>Discs rarely 'warp'. What happens is uneven wear that creates thickness variation around the disc, so the pads grip more in some places than others. Heavy braking followed by holding the pedal at a standstill, common in traffic, imprints pad material onto hot discs and starts the cycle.</p>
<h2>Cause two: hub run-out</h2>
<p>If the hub face or a wheel bearing is worn, a perfect new disc will run out of true and wear unevenly within weeks. We measure hub run-out with a dial gauge before fitting new discs. Skipping this is why some owners replace discs every year.</p>
<h2>Cause three: suspension bushes</h2>
<p>Worn front lower arm bushes allow the wheel to shimmy under braking load, felt as judder even with perfect discs. It is more common on the Sport than the full-size Range Rover because of the stiffer setup.</p>
<h2>The right repair</h2>
<p>Measure, then replace. Quality discs from Brembo or genuine Land Rover, matching pads, bedded in correctly, on hubs that have been checked. It costs slightly more than a quick swap and lasts several times longer.</p>"""),
 dict(slug="terrain-response-explained", title="Terrain Response Explained: What Each Mode Actually Changes", date="2026-03-25", cat="Off-Road", read=6,
  excerpt="The rotary dial does far more than change a dashboard icon. Here is what happens to the throttle, gearbox, differentials and suspension in each setting.",
  body="""<p>Every Land Rover since the Discovery 3 has carried Terrain Response, and most owners use it in exactly one mode. That is a shame, because understanding what the system does makes both on-road and desert driving safer and less stressful for the vehicle.</p>
<h2>General</h2>
<p>The default. Balanced throttle mapping, normal ride height, differentials open until slip is detected.</p>
<h2>Grass, Gravel, Snow</h2>
<p>Softens throttle response so a heavy foot does not spin the wheels, starts in second gear, and biases traction control to intervene early. Ideal for wet roads after rare rain.</p>
<h2>Mud and Ruts</h2>
<p>Raises the suspension, allows more wheel slip before traction control acts so the tyres can clear themselves, and pre-loads the centre differential.</p>
<h2>Sand</h2>
<p>The mode that matters here. Throttle becomes sharper, gear changes are held longer to keep the engine in its torque band, traction control permits significant slip so the vehicle can keep momentum, and the suspension rises. Combined with lowered tyre pressures, this is what makes a Range Rover effortless on the dunes.</p>
<h2>Rock Crawl</h2>
<p>Low range only. Maximum ride height, very gentle throttle, differentials locked, hill descent control engaged.</p>
<h2>A note on faults</h2>
<p>A 'Terrain Response not available' message usually points to an air suspension, ABS or transfer box fault rather than the switch itself. Our diagnostic check pinpoints which.</p>"""),
]

TESTIMONIALS = [
 ("My Range Rover Sport was sinking every night and two garages had already replaced the compressor. Al Rahal found a cracked rear strut in twenty minutes. Fixed the same day and it has been perfect for a year.", "Khalid A.", "Range Rover Sport SDV6"),
 ("Timing chain rattle on my Discovery 4. They showed me the stretch measurement on the diagnostic screen before doing anything, gave me a fixed price and had the car back in three days. Silent now.", "Sarah M.", "Discovery 4 3.0 TDV6"),
 ("The dealer quoted a new gearbox. Al Rahal repaired the mechatronic unit for a fraction of the price and my Vogue shifts like new. Honest people.", "Rashid H.", "Range Rover Vogue 5.0 SC"),
 ("I use them for my Velar and my wife's Evoque. Everything on WhatsApp, photos of every job, no surprises on the invoice.", "Daniel O.", "Range Rover Velar P250"),
]

GENERAL_FAQ = [
 ("Do you only work on Range Rover and Land Rover?","Range Rover and Land Rover are our speciality and the majority of our work, but we also service BMW, Mercedes-Benz, Audi, Porsche, Jaguar, Bentley and Rolls-Royce with the correct diagnostic equipment for each brand."),
 ("Will servicing at Al Rahal affect my manufacturer warranty?","No. We use genuine parts, follow the manufacturer's schedule and update your online service record, which keeps your warranty valid."),
 ("How do I book?","Tap any WhatsApp button on this site, or message 055 747 9292 with your model, year and the issue. We reply within minutes during working hours and confirm a time."),
 ("Do you offer pick-up and delivery?","Yes, we offer vehicle collection and return within the city. Ask on WhatsApp when booking."),
 ("Do you provide a warranty on repairs?","All repairs carry a parts and labour warranty. The term is stated on your invoice before work begins."),
 ("Can I wait while my car is serviced?","Yes. Our customer lounge has fast Wi-Fi, coffee and a view into the workshop so you can watch the work being done."),
 ("Do you use genuine parts?","Yes. We use genuine Land Rover parts by default, and where a high-quality OE-equivalent from the original manufacturer offers better value we will explain the choice and let you decide."),
]

GALLERY = [
 ("gallery-01.jpg","Range Rover Vogue on the alignment ramp"),("gallery-02.jpg","5.0 V8 supercharger removed for coolant pipe upgrade"),
 ("gallery-03.jpg","Air suspension strut replacement"),("gallery-04.jpg","Diagnostic session with Land Rover Pathfinder"),
 ("gallery-05.jpg","ZF gearbox valve body on the bench"),("gallery-06.jpg","Timing chain replacement on a TDV6"),
 ("gallery-07.jpg","Customer lounge with workshop view"),("gallery-08.jpg","Defender prepared for a desert expedition"),
 ("gallery-09.jpg","Ceramic coating in the detailing studio"),("gallery-10.jpg","Genuine parts store"),
]
