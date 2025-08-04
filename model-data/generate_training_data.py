import os
import csv
from collections import defaultdict

training_data = {
    "dataset": [ # [cite: 116]
        ("pothole on main road needs fixing", "Road Maintenance"),
        ("broken streetlight near school", "Street Lighting"),
        ("we need sidewalks on Maple Street", "Sidewalk Construction"),
        ("bridge railing is damaged", "Bridge Repair"),
        ("storm drain is clogged with debris", "Drainage Maintenance"),
        ("traffic signal not working properly", "Traffic Signal Repair"),
        ("road signs are faded and unreadable", "Road Signage"),
        ("pedestrian crosswalk paint is worn off", "Crosswalk Maintenance"),
        ("manhole cover is missing", "Road Safety"),
        ("construction debris blocking road", "Road Obstruction"),
        # New 
        ("large crack forming on highway lane", "Road Maintenance"),
        ("flickering streetlights on Oak Avenue", "Street Lighting"),
        ("missing curb ramps for wheelchair access", "Sidewalk Construction"),
        ("corroded support beams under bridge", "Bridge Repair"),
        ("standing water on road after rain", "Drainage Maintenance"),
        ("left-turn signal timing too short", "Traffic Signal Repair"),
        ("missing stop sign at dangerous intersection", "Road Signage"),
        ("faded bike lane markings causing confusion", "Crosswalk Maintenance"),
        ("loose gravel on road causing accidents", "Road Safety"),
        ("abandoned vehicle obstructing traffic", "Road Obstruction"),
        ("uneven road surface damaging vehicles", "Road Maintenance"),
        ("dark stretch of road needs more lighting", "Street Lighting"),
        ("cracked sidewalk tiles near park entrance", "Sidewalk Construction"),
        ("bridge expansion joint failure", "Bridge Repair"),
        ("clogged catch basins during storms", "Drainage Maintenance"),
        ("malfunctioning pedestrian walk signal", "Traffic Signal Repair"),
        ("missing school zone warning signs", "Road Signage"),
        ("worn pedestrian crossing near market", "Crosswalk Maintenance"),
        ("exposed rebar on road divider", "Road Safety"),
        ("unmarked construction zone hazards", "Road Obstruction"),
        ("multiple potholes on Highway 42 causing tire damage", "Road Maintenance"),
        ("streetlights on Pine Street not activating after sunset", "Street Lighting"),
        ("request for sidewalk repair near downtown library", "Sidewalk Construction"),
        ("cracks appearing on overpass support columns", "Bridge Repair"),
        ("persistent flooding on Elm Blvd after moderate rain", "Drainage Maintenance"),
        ("left-turn signal at Oak and 5th not detected by vehicles", "Traffic Signal Repair"),
        ("missing 'No Parking' signs in front of fire station", "Road Signage"),
        ("pedestrian crossing near school lacks audible signals", "Crosswalk Maintenance"),
        ("exposed wiring on road dividers poses electrocution risk", "Road Safety"),
        ("construction materials left on Main Street overnight", "Road Obstruction"),
        ("sinkhole developing on Riverside Drive", "Road Maintenance"),
        ("inconsistent brightness of LED streetlights on Maple Ave", "Street Lighting"),
        ("uneven sidewalk slabs causing tripping hazards", "Sidewalk Construction"),
        ("corroded bolts on suspension bridge", "Bridge Repair"),
        ("drainage grates missing in shopping district", "Drainage Maintenance"),
        ("traffic lights out of sync during rush hour", "Traffic Signal Repair"),
        ("obscured stop sign by overgrown bushes", "Road Signage"),
        ("faded pedestrian crossing near bus terminal", "Crosswalk Maintenance"),
        ("lack of reflective markers on sharp curves", "Road Safety"),
        ("abandoned construction equipment blocking lane", "Road Obstruction"),
        ("recurring potholes on exit ramp of Interstate 90", "Road Maintenance"),
        ("flickering street lamps creating strobe effect on Cedar Ave", "Street Lighting"),
        ("missing ADA-compliant ramps at 3rd St intersections", "Sidewalk Construction"),
        ("concrete spalling on bridge underside near Pier 12", "Bridge Repair"),
        ("chronic water pooling at Market St/5th Ave intersection", "Drainage Maintenance"),
        ("right-turn arrow signal stuck on red during peak hours", "Traffic Signal Repair"),
        ("'School Zone' sign knocked down by storm last week", "Road Signage"),
        ("crosswalk countdown timer malfunctioning at busy plaza", "Crosswalk Maintenance"),
        ("unprotected excavation site near playground entrance", "Road Safety"),
        ("road closure signs not removed after project completion", "Road Obstruction"),
        ("alligator cracking spreading across parking lot exit", "Road Maintenance"), 
        ("dark zone between streetlights on bike path stretch", "Street Lighting"),
        ("tree roots uplifting sidewalk panels on Willow Lane", "Sidewalk Construction"),
        ("rusted expansion joints causing bridge deck vibration", "Bridge Repair"),
        ("standing water breeding mosquitoes in suburban cul-de-sac", "Drainage Maintenance"),
        ("pedestrian push buttons unresponsive at multiple crossings", "Traffic Signal Repair"),
        ("graffiti obscuring speed limit signs near school zone", "Road Signage"),
        ("reflective crosswalk studs missing after repaving work", "Crosswalk Maintenance"),
        ("unmarked temporary trench across pedestrian pathway", "Road Safety"),
        ("roadside construction barriers improperly secured", "Road Obstruction")

        # Education Department
        ("no benches in the classroom", "Classroom Infrastructure"),
        ("school roof is leaking during rain", "Building Maintenance"),
        ("playground equipment is broken", "Playground Maintenance"),
        ("no proper drinking water in school", "School Facilities"),
        ("library books are very old", "Educational Resources"),
        ("computer lab has no working computers", "Technology Infrastructure"),
        ("school bus is always late", "Transportation Services"),
        ("no proper toilets for girls", "Sanitation Facilities"),
        ("teachers are frequently absent", "Staff Management"),
        ("no electricity in some classrooms", "Utility Services"),
        # New entries
        ("collapsing ceiling tiles in science lab", "Classroom Infrastructure"),
        ("broken window panes in classroom", "Building Maintenance"),
        ("rusted swings in playground", "Playground Maintenance"),
        ("contaminated water supply in cafeteria", "School Facilities"),
        ("outdated geography textbooks", "Educational Resources"),
        ("no internet connectivity in computer lab", "Technology Infrastructure"),
        ("school bus breakdowns becoming frequent", "Transportation Services"),
        ("toilet doors missing locks", "Sanitation Facilities"),
        ("substitute teachers not provided", "Staff Management"),
        ("frequent power surges damaging equipment", "Utility Services"),
        ("broken desk legs causing injuries", "Classroom Infrastructure"),
        ("mold growth in classroom walls", "Building Maintenance"),
        ("sharp edges on playground slide", "Playground Maintenance"),
        ("non-functional water coolers", "School Facilities"),
        ("insufficient chemistry lab equipment", "Educational Resources"),
        ("projector systems outdated", "Technology Infrastructure"),
        ("bus routes not covering new neighborhoods", "Transportation Services"),
        ("toilet plumbing frequently clogged", "Sanitation Facilities"),
        ("lack of special education staff", "Staff Management"),
        ("inconsistent heating in winter", "Utility Services"),
        ("loose wiring posing hazards in classrooms", "Classroom Infrastructure"),
        ("cracks appearing on school building walls", "Building Maintenance"),
        ("playground ground uneven causing falls", "Playground Maintenance"),
        ("water fountains leaking in hallways", "School Facilities"),
        ("outdated library computer systems", "Educational Resources"),
        ("broken keyboards in computer lab", "Technology Infrastructure"),
        ("school bus drivers not following safety protocols", "Transportation Services"),
        ("no sanitary napkin disposal bins in toilets", "Sanitation Facilities"),
        ("teachers arriving late regularly", "Staff Management"),
        ("classrooms lack fans or ventilation", "Utility Services"),
        ("desks overcrowded, not enough for students", "Classroom Infrastructure"),
        ("roof tiles missing after storm", "Building Maintenance"),
        ("playground fencing damaged and unsafe", "Playground Maintenance"),
        ("cafeteria water cooler out of service", "School Facilities"),
        ("library shelves broken and unstable", "Educational Resources"),
        ("network issues disrupting computer classes", "Technology Infrastructure"),
        ("bus stops lacking shelters or benches", "Transportation Services"),
        ("toilets emitting foul smell due to poor drainage", "Sanitation Facilities"),
        ("shortage of qualified special education teachers", "Staff Management"),
        ("electricity outages causing class disruptions", "Utility Services"),
        ("chalkboards damaged and unusable", "Classroom Infrastructure"),
        ("mildew on walls causing health issues", "Building Maintenance"),
        ("swing chains rusted and unsafe", "Playground Maintenance"),
        ("broken taps in school washrooms", "School Facilities"),
        ("computers missing essential software", "Educational Resources"),
        ("frequent breakdowns of projector units", "Technology Infrastructure"),
        ("school buses with broken seat belts", "Transportation Services"),
        ("toilets lacking running water", "Sanitation Facilities"),
        ("lack of teacher training on new curricula", "Staff Management"),
        ("insufficient lighting in classrooms", "Utility Services"),
        ("holes in classroom doors", "Classroom Infrastructure"),
        ("crumbling plaster on walls", "Building Maintenance"),
        ("playground surface slippery after rain", "Playground Maintenance"),
        ("water tanks not cleaned regularly", "School Facilities"),
        ("damaged computer monitors", "Educational Resources"),
        ("wireless internet speed too slow for classes", "Technology Infrastructure"),
        ("bus routes not synchronized with school timings", "Transportation Services"),
        ("toilet paper often unavailable in restrooms", "Sanitation Facilities"),
        ("teachers lacking access to teaching aids", "Staff Management"),
        ("poor heating system making classrooms cold", "Utility Services"),
    
        # Revenue Department
        ("delay in property tax assessment", "Property Tax Issues"),
        ("incorrect land record entry", "Land Record Discrepancies"),
        ("difficulty obtaining trade license", "License Application Delays"),
        ("overcharged for stamp duty", "Stamp Duty Concerns"),
        ("problem with income certificate issuance", "Certificate Issuance"),
        ("mutation process taking too long", "Property Mutation Delays"),
        ("non-receipt of tax refund", "Tax Refund Issues"),
        ("dispute over property valuation", "Property Valuation Disputes"),
        ("unable to update land ownership details", "Land Ownership Updates"),
        ("questions about commercial tax rates", "Commercial Tax Inquiry"),
        # New entries
        ("property tax bill not received for current fiscal year", "Property Tax Issues"),
        ("error in land survey map coordinates", "Land Record Discrepancies"),
        ("repeated document submissions for license renewal", "License Application Delays"),
        ("stamp duty exemption eligibility confusion", "Stamp Duty Concerns"),
        ("delay in caste certificate verification", "Certificate Issuance"),
        ("missing signature approval on mutation papers", "Property Mutation Delays"),
        ("GST refund stuck processing for 3 months", "Tax Refund Issues"),
        ("dispute over agricultural land valuation", "Property Valuation Disputes"),
        ("inheritance details not updated in records", "Land Ownership Updates"),
        ("clarification needed on hotel tax slabs", "Commercial Tax Inquiry"),
        ("incorrect tax calculation for vacant land", "Property Tax Issues"),
        ("boundary dispute due to outdated land records", "Land Record Discrepancies"),
        ("online trade license portal technical errors", "License Application Delays"),
        ("double charged for property registration stamp duty", "Stamp Duty Concerns"),
        ("income certificate rejected without valid reason", "Certificate Issuance"),
        ("mutation application lost by office staff", "Property Mutation Delays"),
        ("TDS refund delay despite proper documentation", "Tax Refund Issues"),
        ("valuation mismatch between buyer and department", "Property Valuation Disputes"),
        ("joint ownership not reflected in records", "Land Ownership Updates"),
        ("query about tax incentives for startups", "Commercial Tax Inquiry"),
        ("property tax notice not delivered despite payment", "Property Tax Issues"),
        ("land record details inconsistent between departments", "Land Record Discrepancies"),
        ("license renewal date changed without notification", "License Application Delays"),
        ("confusion over stamp duty slabs for commercial properties", "Stamp Duty Concerns"),
        ("delay in issuance of income and domicile certificates", "Certificate Issuance"),
        ("mutation request pending for over 6 months", "Property Mutation Delays"),
        ("tax refund amount incorrectly credited to another account", "Tax Refund Issues"),
        ("disagreement over property valuation in rural areas", "Property Valuation Disputes"),
        ("failure to update joint ownership after inheritance", "Land Ownership Updates"),
        ("queries about commercial tax registration process", "Commercial Tax Inquiry"),
        ("property tax calculated on outdated property data", "Property Tax Issues"),
        ("land record entries missing critical documents", "Land Record Discrepancies"),
        ("website crashes during online license application", "License Application Delays"),
        ("stamp duty receipt not issued after payment", "Stamp Duty Concerns"),
        ("certificate issuance delayed due to staff shortage", "Certificate Issuance"),
        ("mutation fees paid but no status update", "Property Mutation Delays"),
        ("refund claim rejected without explanation", "Tax Refund Issues"),
        ("valuation disputes delaying property sale", "Property Valuation Disputes"),
        ("land ownership records not reflecting recent sale", "Land Ownership Updates"),
        ("inquiries about tax benefits for new entrepreneurs", "Commercial Tax Inquiry"),
        ("property tax exemption application rejected wrongly", "Property Tax Issues"),
        ("old land records not digitized causing delays", "Land Record Discrepancies"),
        ("license documents lost during renewal process", "License Application Delays"),
        ("stamp duty payments not reflected in system", "Stamp Duty Concerns"),
        ("certificate application rejected due to incorrect details", "Certificate Issuance"),
        ("mutation application submitted but not acknowledged", "Property Mutation Delays"),
        ("refund application stuck in verification stage", "Tax Refund Issues"),
        ("conflict over valuation between buyer and bank", "Property Valuation Disputes"),
        ("land ownership changes not updated after court orders", "Land Ownership Updates"),
        ("questions regarding commercial tax return deadlines", "Commercial Tax Inquiry"),
        ("property tax portal showing incorrect due amounts", "Property Tax Issues"),
        ("survey map errors causing ownership conflicts", "Land Record Discrepancies"),
        ("delay in processing new trade licenses", "License Application Delays"),
        ("stamp duty recalculation demanded after payment", "Stamp Duty Concerns"),
        ("delay in income certificate renewal", "Certificate Issuance"),
        ("mutation documents misplaced by municipal office", "Property Mutation Delays"),
        ("tax refund under process for more than 6 months", "Tax Refund Issues"),
        ("valuation report not shared with applicant", "Property Valuation Disputes"),
        ("land ownership certificate issuance delayed", "Land Ownership Updates"),
        ("clarification needed on commercial tax penalties", "Commercial Tax Inquiry"),
        ("property tax notices sent to wrong address", "Property Tax Issues"),
        ("incomplete land records affecting property registration", "Land Record Discrepancies"),
        ("license application stuck in technical review", "License Application Delays"),

        # Health Department
        ("clinic has no running water", "Facility Maintenance"),
        ("hospital staff is rude to patients", "Staff Behavior"),
        ("long waiting times at government hospital", "Service Efficiency"),
        ("medicines not available at PHC", "Medical Supplies"),
        ("ambulance service is very slow", "Emergency Services"),
        ("dirty conditions in hospital ward", "Hygiene Standards"),
        ("medical equipment not working", "Equipment Maintenance"),
        ("no proper parking at hospital", "Infrastructure Issues"),
        ("vaccination program not reaching villages", "Public Health Programs"),
        ("no specialist doctors available", "Medical Staff"),
        # New entries
        ("broken X-ray machine in clinic", "Equipment Maintenance"),
        ("patients forced to buy gloves from outside", "Medical Supplies"),
        ("emergency ward understaffed during nights", "Medical Staff"),
        ("used syringes left in open bins", "Hygiene Standards"),
        ("no wheelchair ramps in new hospital wing", "Facility Maintenance"),
        ("paramedics arriving late to emergency calls", "Emergency Services"),
        ("corrupted vaccine cold storage system", "Public Health Programs"),
        ("long wait times for pediatric appointments", "Service Efficiency"),
        ("security guards harassing visitors", "Staff Behavior"),
        ("insufficient ICU beds during flu season", "Infrastructure Issues"),
        ("expired medicines dispensed to patients", "Medical Supplies"),
        ("non-functional fire safety systems", "Facility Maintenance"),
        ("dialysis machines frequently breaking down", "Equipment Maintenance"),
        ("mosquito breeding in hospital premises", "Hygiene Standards"),
        ("no gynecologist available at rural clinic", "Medical Staff"),
        ("ambulance drivers refusing night shifts", "Emergency Services"),
        ("malaria prevention campaign delayed", "Public Health Programs"),
        ("elderly patients waiting hours for consultation", "Service Efficiency"),
        ("rude behavior from pharmacy staff", "Staff Behavior"),
        ("insufficient parking for disabled visitors", "Infrastructure Issues"),
        ("peeled paint and damp walls in hospital corridor", "Facility Maintenance"),
        ("reception staff yelling at patients", "Staff Behavior"),
        ("routine checkups taking over 5 hours", "Service Efficiency"),
        ("basic medicines out of stock for weeks", "Medical Supplies"),
        ("ambulance refused to come without advance payment", "Emergency Services"),
        ("filthy toilets in emergency ward", "Hygiene Standards"),
        ("ventilators not working in critical care", "Equipment Maintenance"),
        ("poor lighting in hospital parking area", "Infrastructure Issues"),
        ("immunization van failed to visit scheduled village", "Public Health Programs"),
        ("ENT specialist absent for a month", "Medical Staff"),
        ("power backup fails during operations", "Facility Maintenance"),
        ("doctor shouting at senior citizen", "Staff Behavior"),
        ("queues spilling outside hospital gate", "Service Efficiency"),
        ("antibiotics not available in dispensary", "Medical Supplies"),
        ("no ambulance available during local festival", "Emergency Services"),
        ("bio-waste dumped in open near clinic", "Hygiene Standards"),
        ("MRI scanner under maintenance for weeks", "Equipment Maintenance"),
        ("cracked tiles and slippery floors in OPD", "Infrastructure Issues"),
        ("malnutrition survey team never arrived", "Public Health Programs"),
        ("no pediatrician in government clinic", "Medical Staff"),
        ("emergency ward roof leaking during rain", "Facility Maintenance"),
        ("nurses being rude to tribal patients", "Staff Behavior"),
        ("lab reports delayed by several days", "Service Efficiency"),
        ("painkillers not available in hospital store", "Medical Supplies"),
        ("ambulance refused to carry unconscious person", "Emergency Services"),
        ("unclean bed sheets and foul smell in wards", "Hygiene Standards"),
        ("CT scan machine unavailable due to malfunction", "Equipment Maintenance"),
        ("no signage for departments in hospital", "Infrastructure Issues"),
        ("health awareness campaign cancelled without notice", "Public Health Programs"),
        ("radiologist not reporting to duty", "Medical Staff"),
        ("operation theatre lights not working properly", "Facility Maintenance"),
        ("staff mocking patients in local dialect", "Staff Behavior"),
        ("ultrasound appointments delayed by months", "Service Efficiency"),
        ("antiseptic creams out of stock", "Medical Supplies"),
        ("ambulance lacks basic first aid kits", "Emergency Services"),
        ("overflowing bins in outpatient lobby", "Hygiene Standards"),
        ("defibrillator not charged in emergency room", "Equipment Maintenance"),
        ("outdoor clinic lacks waiting area", "Infrastructure Issues"),
        ("rural TB awareness drive skipped villages", "Public Health Programs"),
        ("government clinic has no dermatology expert", "Medical Staff"),
        ("gurney wheels broken in trauma center", "Facility Maintenance"),
        ("compounder shouting at senior citizens", "Staff Behavior"),
        ("patients forced to stand for hours", "Service Efficiency"),
        ("no cough syrups for children available", "Medical Supplies"),
        ("ambulance delayed due to driver absence", "Emergency Services"),
        ("hospital kitchen attracts flies and rodents", "Hygiene Standards"),
        ("ECG machine broken for over a week", "Equipment Maintenance"),
        ("no fire exits marked in hospital building", "Infrastructure Issues"),

        # Water Supply and Sanitation
        ("no water supply for three days", "Water Supply Outage"),
        ("contaminated drinking water", "Water Quality Issues"),
        ("leaking water pipe on street", "Pipe Leakage"),
        ("overflowing sewage drain", "Sewage Overflow"),
        ("request for new water connection", "New Water Connection"),
        ("clogged public toilet", "Public Toilet Maintenance"),
        ("irregular garbage collection from sanitation dept", "Waste Collection Irregularity"),
        ("broken hand pump in community area", "Hand Pump Repair"),
        ("low water pressure in taps", "Low Water Pressure"),
        ("need for better drainage in our locality", "Drainage Improvement Request"),
        # New entries
        ("foul smell from water treatment plant", "Water Quality Issues"),
        ("sewage mixing with drinking water lines", "Sewage Overflow"),
        ("illegal connections draining water pressure", "Low Water Pressure"),
        ("public toilet doors broken for weeks", "Public Toilet Maintenance"),
        ("garbage trucks leaking waste during transport", "Waste Collection Irregularity"),
        ("rust-colored water from household taps", "Water Quality Issues"),
        ("burst pipeline flooding residential area", "Pipe Leakage"),
        ("delay in approving borewell permission", "New Water Connection"),
        ("hand pump handle missing after repair", "Hand Pump Repair"),
        ("water logging due to blocked storm drains", "Drainage Improvement Request"),
        ("intermittent water supply during summers", "Water Supply Outage"),
        ("algae growth in municipal water tank", "Water Quality Issues"),
        ("sewage backup into basement parking", "Sewage Overflow"),
        ("public toilet water tanks empty", "Public Toilet Maintenance"),
        ("uncollected garbage attracting stray animals", "Waste Collection Irregularity"),
        ("air valves leaking at water distribution point", "Pipe Leakage"),
        ("new apartment complex water connection denied", "New Water Connection"),
        ("hand pump contamination from nearby septic tank", "Hand Pump Repair"),
        ("insufficient water pressure in upper floors", "Low Water Pressure"),
        ("standing water causing mosquito breeding", "Drainage Improvement Request"),
        ("entire block receiving muddy water", "Water Quality Issues"),
        ("pipe burst near school unattended for days", "Pipe Leakage"),
        ("frequent water cuts without notice", "Water Supply Outage"),
        ("foul odor in tap water", "Water Quality Issues"),
        ("clogged sewer outside market area", "Sewage Overflow"),
        ("illegal water tapping from mainline", "Low Water Pressure"),
        ("non-functional toilet lights in public facility", "Public Toilet Maintenance"),
        ("overflowing garbage bins near sanitation office", "Waste Collection Irregularity"),
        ("broken valve spraying water on road", "Pipe Leakage"),
        ("application for connection not acknowledged", "New Water Connection"),
        ("children unable to use broken hand pump", "Hand Pump Repair"),
        ("water just trickling from taps on 3rd floor", "Low Water Pressure"),
        ("no drains in newly built road", "Drainage Improvement Request"),
        ("leaking tank supplying dirty water", "Water Quality Issues"),
        ("sewage overflows after every rainfall", "Sewage Overflow"),
        ("doors missing in public urinals", "Public Toilet Maintenance"),
        ("garbage collection missed on alternate days", "Waste Collection Irregularity"),
        ("constant leakage at pipe joint on main road", "Pipe Leakage"),
        ("pending connection for newly built house", "New Water Connection"),
        ("hand pump makes metallic grinding sound", "Hand Pump Repair"),
        ("pressure drop during peak hours", "Low Water Pressure"),
        ("no proper drainage in new colony", "Drainage Improvement Request"),
        ("worms found in supplied drinking water", "Water Quality Issues"),
        ("sewage smell in entire apartment block", "Sewage Overflow"),
        ("flush systems broken in public restrooms", "Public Toilet Maintenance"),
        ("garbage scattered around collection point", "Waste Collection Irregularity"),
        ("pipeline leak damaging house foundation", "Pipe Leakage"),
        ("connection papers lost at municipal office", "New Water Connection"),
        ("hand pump jammed after partial repair", "Hand Pump Repair"),
        ("water stops completely by noon daily", "Low Water Pressure"),
        ("rainwater stagnation due to clogged culvert", "Drainage Improvement Request"),
        ("black particles in water storage tanks", "Water Quality Issues"),
        ("overflowing septic tanks behind complex", "Sewage Overflow"),
        ("handwashing stations broken at toilets", "Public Toilet Maintenance"),
        ("waste not collected in commercial area", "Waste Collection Irregularity"),
        ("persistent leakage at underground pipeline", "Pipe Leakage"),
        ("waiting 3 months for new water tap approval", "New Water Connection"),
        ("handle of hand pump spins without pumping", "Hand Pump Repair"),
        ("ground floor pressure okay, upper floors dry", "Low Water Pressure"),
        ("roadside ditch turns into stagnant water pool", "Drainage Improvement Request"),
        ("pipeline corrosion causing brownish water", "Water Quality Issues"),

        # Electricity and Power
        ("frequent power cuts in my area", "Power Outages"),
        ("electricity bill is excessively high", "Billing Errors"),
        ("fallen electricity pole dangerous", "Damaged Infrastructure"),
        ("voltage fluctuation damaging appliances", "Voltage Fluctuation"),
        ("delay in new electricity meter installation", "New Connection Delay"),
        ("transformer sparking near residential area", "Transformer Issues"),
        ("street lights not working on our road (power issue)", "Street Lighting Power"),
        ("unauthorized electricity connection", "Power Theft"),
        ("request for tree trimming near power lines", "Power Line Maintenance"),
        ("meter reading seems incorrect", "Meter Reading Dispute"),
        # New entries
        ("partial phase failure causing equipment damage", "Voltage Fluctuation"),
        ("overhead wires dangerously low over road", "Damaged Infrastructure"),
        ("smart meter showing phantom usage", "Billing Errors"),
        ("transformer explosion causing blackout", "Power Outages"),
        ("meter replacement delayed by 2 months", "New Connection Delay"),
        ("illegal hooking from main distribution line", "Power Theft"),
        ("flickering street lights causing accidents", "Street Lighting Power"),
        ("overgrown branches touching live wires", "Power Line Maintenance"),
        ("three-phase supply not activated for industry", "New Connection Delay"),
        ("meter serial number mismatch in bills", "Meter Reading Dispute"),
        ("brownouts damaging refrigerator compressor", "Voltage Fluctuation"),
        ("cracked insulator on transmission tower", "Damaged Infrastructure"),
        ("double charging for solar power surplus", "Billing Errors"),
        ("weekly 8-hour outages in industrial zone", "Power Outages"),
        ("transformer humming noise disturbing residents", "Transformer Issues"),
        ("theft of copper wires from substation", "Power Theft"),
        ("inconsistent street light timings", "Street Lighting Power"),
        ("tree branch fell on power line during storm", "Power Line Maintenance"),
        ("no response to online connection request", "New Connection Delay"),
        ("estimated billing despite meter installation", "Meter Reading Dispute"),
        ("entire lane facing blackout every evening", "Power Outages"),
        ("frequent night-time outages affecting sleep", "Power Outages"),
        ("bill includes unexplained fixed charges", "Billing Errors"),
        ("sudden hike in units despite no increase in usage", "Billing Errors"),
        ("cracked pole base swaying dangerously", "Damaged Infrastructure"),
        ("burnt wire hanging from pole", "Damaged Infrastructure"),
        ("TV damaged due to voltage surge", "Voltage Fluctuation"),
        ("low voltage preventing motor from running", "Voltage Fluctuation"),
        ("application for new meter not acknowledged", "New Connection Delay"),
        ("commercial connection wrongly installed for residence", "New Connection Delay"),
        ("transformer oil leaking on footpath", "Transformer Issues"),
        ("buzzing noise from nearby transformer", "Transformer Issues"),
        ("entire street in darkness for a week", "Street Lighting Power"),
        ("street light poles rusted and unstable", "Street Lighting Power"),
        ("unauthorized connections seen in slum area", "Power Theft"),
        ("power tapped illegally from overhead cables", "Power Theft"),
        ("branches growing between HV lines", "Power Line Maintenance"),
        ("request for urgent trimming before storm season", "Power Line Maintenance"),
        ("meter number on bill does not match actual meter", "Meter Reading Dispute"),
        ("billed for units higher than recorded", "Meter Reading Dispute"),
        ("scheduled maintenance outages not informed", "Power Outages"),
        ("billing portal shows wrong consumption history", "Billing Errors"),
        ("tilted electric pole leaning toward house", "Damaged Infrastructure"),
        ("cable joints exposed and unsecured", "Damaged Infrastructure"),
        ("AC unit keeps restarting due to voltage dips", "Voltage Fluctuation"),
        ("voltage too high during night hours", "Voltage Fluctuation"),
        ("new connection sanctioned but not energized", "New Connection Delay"),
        ("consumer number not generated after registration", "New Connection Delay"),
        ("transformer placed too close to children's park", "Transformer Issues"),
        ("low hanging service wire touching vehicles", "Damaged Infrastructure"),
        ("street lights stay on during daytime", "Street Lighting Power"),
        ("lights blink continuously and confuse drivers", "Street Lighting Power"),
        ("unauthorized wiring on electric poles", "Power Theft"),
        ("agriculture pump running on illegal connection", "Power Theft"),
        ("loose branches swaying on overhead line", "Power Line Maintenance"),
        ("creepers climbing onto service wires", "Power Line Maintenance"),
        ("bill generated on average basis despite meter access", "Meter Reading Dispute"),
        ("wrong consumer category billed", "Billing Errors"),
        ("outage after rain not restored for hours", "Power Outages"),
        ("transformer placement blocking footpath", "Transformer Issues"),
        ("lights out on school road after dusk", "Street Lighting Power"),
        ("line snapped by tree still unrepaired", "Power Line Maintenance"),

        # Transportation
        ("city buses are overcrowded and infrequent", "Public Bus Service"),
        ("auto-rickshaw driver refused to use meter", "Fare Meter Issues"),
        ("poor condition of bus stops", "Bus Stop Maintenance"),
        ("traffic congestion at XYZ junction daily", "Traffic Management"),
        ("need for speed breakers in residential zone", "Road Safety Measures"),
        ("application for driving license pending", "Driving License Issues"),
        ("damaged road signs causing confusion (transport focus)", "Transport Road Signage"),
        ("illegal parking blocking traffic flow", "Illegal Parking"),
        ("request for new bus route to industrial area", "Bus Route Request"),
        ("overloading of commercial vehicles", "Vehicle Overloading"),
        # New entries
        ("bus drivers skipping scheduled stops", "Public Bus Service"),
        ("prepaid auto counters not functioning", "Fare Meter Issues"),
        ("broken shelter at main bus terminal", "Bus Stop Maintenance"),
        ("unregulated hawkers occupying traffic islands", "Traffic Management"),
        ("missing guardrails on mountain road", "Road Safety Measures"),
        ("learner's license verification delay", "Driving License Issues"),
        ("missing diversion signs during roadwork", "Transport Road Signage"),
        ("trucks parked illegally on highway shoulders", "Illegal Parking"),
        ("petition for night bus service to airport", "Bus Route Request"),
        ("overloaded gravel trucks spilling debris", "Vehicle Overloading"),
        ("elderly passengers denied bus seating", "Public Bus Service"),
        ("shared autos charging double at night", "Fare Meter Issues"),
        ("no lighting at rural bus stand", "Bus Stop Maintenance"),
        ("school zone traffic chaos during dismissal", "Traffic Management"),
        ("request for cat-eye reflectors on curves", "Road Safety Measures"),
        ("international license conversion issues", "Driving License Issues"),
        ("vandalized direction signs on highway", "Transport Road Signage"),
        ("cars parked in no-parking zone near hospital", "Illegal Parking"),
        ("demand for express bus to tech park", "Bus Route Request"),
        ("overloaded school vans risking safety", "Vehicle Overloading"),
        # 37 new entries
        ("frequent delays in city bus timetable", "Public Bus Service"),
        ("bus drivers behaving rudely with commuters", "Public Bus Service"),
        ("meter tampering reported in autos", "Fare Meter Issues"),
        ("taxi drivers not accepting digital payments", "Fare Meter Issues"),
        ("bus stop lacks seating and shelter", "Bus Stop Maintenance"),
        ("no signboards at major bus terminals", "Bus Stop Maintenance"),
        ("signal timing imbalance causing gridlock", "Traffic Management"),
        ("intersection blocked due to poor traffic planning", "Traffic Management"),
        ("lack of pedestrian crossings on busy roads", "Road Safety Measures"),
        ("speed breakers absent near school zone", "Road Safety Measures"),
        ("long waiting time at RTO for test slot", "Driving License Issues"),
        ("driving license application portal errors", "Driving License Issues"),
        ("damaged directional boards on city flyover", "Transport Road Signage"),
        ("signage faded at sharp curve", "Transport Road Signage"),
        ("vehicles parked in front of emergency exits", "Illegal Parking"),
        ("unauthorized vehicles occupying bus lanes", "Illegal Parking"),
        ("petition for bus service extension to outskirts", "Bus Route Request"),
        ("new township lacks direct bus connectivity", "Bus Route Request"),
        ("tractor-trailers overloaded with bricks", "Vehicle Overloading"),
        ("tempos transporting excess cargo unsafely", "Vehicle Overloading"),
        ("complaint about late night buses not stopping", "Public Bus Service"),
        ("buses running without route numbers", "Public Bus Service"),
        ("auto drivers refusing short-distance rides", "Fare Meter Issues"),
        ("overcharging by private taxi operators", "Fare Meter Issues"),
        ("cracked pavement at major bus stop", "Bus Stop Maintenance"),
        ("bus shelters used for illegal vending", "Bus Stop Maintenance"),
        ("bottlenecks due to poor signal synchronization", "Traffic Management"),
        ("congestion due to lack of traffic volunteers", "Traffic Management"),
        ("accidents due to missing speed limit signs", "Road Safety Measures"),
        ("hazardous road curves lack reflectors", "Road Safety Measures"),
        ("verification delay for permanent license", "Driving License Issues"),
        ("license not updated after online test", "Driving License Issues"),
        ("illegible traffic sign near city entrance", "Transport Road Signage"),
        ("road signage confusing near flyover", "Transport Road Signage"),
        ("cars blocking fire hydrants", "Illegal Parking"),
        ("private buses parked in residential lanes", "Illegal Parking"),
        ("need for shuttle bus to major hospital", "Bus Route Request"),
        ("goods vehicles carrying passengers illegally", "Vehicle Overloading"),

        # Municipal Services
        ("garbage not collected for a week", "Waste Management"),
        ("streets are not swept regularly", "Street Cleaning"),
        ("stray dog menace in the neighborhood", "Animal Control"),
        ("unauthorized construction on public land", "Illegal Encroachment"),
        ("birth certificate application delayed by municipality", "Municipal Certificate Issuance"),
        ("public park is poorly maintained", "Park Maintenance"),
        ("waterlogging after every rain (municipal drainage)", "Municipal Drainage Issues"),
        ("need for pest control in market area", "Pest Control Services"),
        ("broken public benches need repair", "Public Amenities"),
        ("complaint about property tax assessment by municipality", "Municipal Property Tax"),
        # New entries
        ("mixed waste not being segregated", "Waste Management"),
        ("construction dust accumulation on roads", "Street Cleaning"),
        ("stray cattle blocking traffic", "Animal Control"),
        ("encroachment of footpaths by shops", "Illegal Encroachment"),
        ("delay in death certificate issuance", "Municipal Certificate Issuance"),
        ("play equipment broken in children's park", "Park Maintenance"),
        ("stormwater drains emptying into streets", "Municipal Drainage Issues"),
        ("rat infestation in vegetable market", "Pest Control Services"),
        ("vandalized public drinking fountain", "Public Amenities"),
        ("incorrect sq.ft rate applied in tax", "Municipal Property Tax"),
        ("biomedical waste mixed with regular trash", "Waste Management"),
        ("uncleaned festival waste post-Diwali", "Street Cleaning"),
        ("monkey nuisance near residential areas", "Animal Control"),
        ("illegal hoardings on municipal property", "Illegal Encroachment"),
        ("error in marriage certificate details", "Municipal Certificate Issuance"),
        ("dead trees not removed from park", "Park Maintenance"),
        ("drain covers stolen causing hazards", "Municipal Drainage Issues"),
        ("mosquito breeding in stagnant water", "Pest Control Services"),
        ("missing lids on public trash bins", "Public Amenities"),
        ("tax notice for non-existent property", "Municipal Property Tax"),
        # 37 new entries
        ("overflowing dumpsters attracting animals", "Waste Management"),
        ("dustbins not cleared on alternate days", "Waste Management"),
        ("market road unswept for weeks", "Street Cleaning"),
        ("festival litter still uncleared after week", "Street Cleaning"),
        ("herd of stray cows near school", "Animal Control"),
        ("monkeys entering houses and stealing food", "Animal Control"),
        ("illegal sheds built over municipal drains", "Illegal Encroachment"),
        ("vegetable sellers occupying walking paths", "Illegal Encroachment"),
        ("incorrect address on birth certificate", "Municipal Certificate Issuance"),
        ("application for income certificate not processed", "Municipal Certificate Issuance"),
        ("garden lights not functioning in public park", "Park Maintenance"),
        ("overgrown grass and weeds in children’s play area", "Park Maintenance"),
        ("clogged drains flooding street corners", "Municipal Drainage Issues"),
        ("no drainage near roadside leading to flooding", "Municipal Drainage Issues"),
        ("flies and maggots in garbage piles", "Pest Control Services"),
        ("mosquitoes breeding in unused fountains", "Pest Control Services"),
        ("rusty and broken swings in municipal park", "Public Amenities"),
        ("community hall water tap broken", "Public Amenities"),
        ("property tax overcharged for residential zone", "Municipal Property Tax"),
        ("name misspelled in property tax record", "Municipal Property Tax"),
        ("waste not collected from slum areas", "Waste Management"),
        ("public toilet garbage left unattended", "Waste Management"),
        ("alleyways not cleaned after rains", "Street Cleaning"),
        ("daily sweepers absent from our lane", "Street Cleaning"),
        ("packs of dogs fighting in open areas", "Animal Control"),
        ("cattle shelter overflowing and unmanaged", "Animal Control"),
        ("food stalls occupying government sidewalk", "Illegal Encroachment"),
        ("rickshaws permanently parked on pavements", "Illegal Encroachment"),
        ("name mismatch in birth certificate", "Municipal Certificate Issuance"),
        ("certificate issued with incorrect date", "Municipal Certificate Issuance"),
        ("rusted seesaws in public park area", "Park Maintenance"),
        ("fallen tree not cleared from park path", "Park Maintenance"),
        ("manholes left open post-cleaning", "Municipal Drainage Issues"),
        ("storm drains releasing sewage onto street", "Municipal Drainage Issues"),
        ("cockroach infestation in public restrooms", "Pest Control Services"),
        ("rats damaging public utility cables", "Pest Control Services"),
        ("public notice board broken", "Public Amenities"),

        # Police Services
        ("reporting a petty theft in my shop", "Theft Report"),
        ("noise pollution from late-night parties", "Noise Complaint"),
        ("suspicious activity observed in the park", "Suspicious Activity Report"),
        ("request for increased patrolling in our area", "Police Patrolling Request"),
        ("traffic violation by a reckless driver (police matter)", "Traffic Violation Enforcement"),
        ("domestic disturbance reported by neighbor", "Domestic Disturbance Report"),
        ("cybercrime incident, online fraud", "Cybercrime Report"),
        ("missing person report initiation", "Missing Person Report"),
        ("complaint against police officer's conduct", "Police Conduct Complaint"),
        ("need assistance for a public event security from police", "Event Security Police Request"),
        # New entries
        ("chain snatching incident near metro station", "Theft Report"),
        ("loud construction work post-midnight", "Noise Complaint"),
        ("unidentified packages left in mall", "Suspicious Activity Report"),
        ("request for women's safety patrols at night", "Police Patrolling Request"),
        ("drunk driving accident on highway", "Traffic Violation Enforcement"),
        ("child custody dispute turning violent", "Domestic Disturbance Report"),
        ("phishing scam through fake government emails", "Cybercrime Report"),
        ("dementia patient wandered from home", "Missing Person Report"),
        ("officer refusing to file FIR", "Police Conduct Complaint"),
        ("security request for religious procession", "Event Security Police Request"),
        ("repeated burglaries in apartment complex", "Theft Report"),
        ("loudspeaker use beyond permitted hours", "Noise Complaint"),
        ("suspicious drone activity near airport", "Suspicious Activity Report"),
        ("demand for police booth near college", "Police Patrolling Request"),
        ("illegal bike racing on city streets", "Traffic Violation Enforcement"),
        ("elder abuse reported by welfare officer", "Domestic Disturbance Report"),
        ("social media account hacking case", "Cybercrime Report"),
        ("runaway teenager missing for 48 hours", "Missing Person Report"),
        ("bribery demand during vehicle check", "Police Conduct Complaint"),
        ("security coordination for political rally", "Event Security Police Request"),
        # 37 new entries
        ("mobile phone stolen on crowded bus", "Theft Report"),
        ("unauthorized DJ party disturbing neighborhood", "Noise Complaint"),
        ("person loitering around ATM suspiciously", "Suspicious Activity Report"),
        ("frequent chain snatching in market road, need patrolling", "Police Patrolling Request"),
        ("multiple cars jumping red light at junction", "Traffic Violation Enforcement"),
        ("verbal abuse and threats between tenants", "Domestic Disturbance Report"),
        ("online loan app blackmailing with fake legal threats", "Cybercrime Report"),
        ("senior citizen missing from park since morning", "Missing Person Report"),
        ("police officer behaving rudely during routine check", "Police Conduct Complaint"),
        ("need police for crowd control at school function", "Event Security Police Request"),
        ("pickpocketing incident at weekly bazaar", "Theft Report"),
        ("late-night music from wedding tent disturbing sleep", "Noise Complaint"),
        ("abandoned vehicle parked for days near residence", "Suspicious Activity Report"),
        ("request for regular night patrols in crime-prone zone", "Police Patrolling Request"),
        ("rash driving of school van reported by parents", "Traffic Violation Enforcement"),
        ("domestic fight escalating in flat next door", "Domestic Disturbance Report"),
        ("Instagram profile hacked and misused", "Cybercrime Report"),
        ("small child missing after temple visit", "Missing Person Report"),
        ("police not taking harassment complaint seriously", "Police Conduct Complaint"),
        ("require security for college fest", "Event Security Police Request"),
        ("wallet stolen during temple crowd", "Theft Report"),
        ("continuous firecracker noise after deadline", "Noise Complaint"),
        ("individual filming people secretly in park", "Suspicious Activity Report"),
        ("police beat patrol irregular after 10 PM", "Police Patrolling Request"),
        ("rash auto drivers creating nuisance daily", "Traffic Violation Enforcement"),
        ("family fight with threats reported by tenant", "Domestic Disturbance Report"),
        ("scam call demanding money as fake police officer", "Cybercrime Report"),
        ("young boy missing after school hours", "Missing Person Report"),
        ("officer using abusive language during questioning", "Police Conduct Complaint"),
        ("requesting crowd control during election result day", "Event Security Police Request"),
        ("bicycle theft outside railway station", "Theft Report"),
        ("noise from street performance till midnight", "Noise Complaint"),
        ("unknown person surveying homes suspiciously", "Suspicious Activity Report"),
        ("ladies hostel requests late night beat patrols", "Police Patrolling Request"),
        ("school bus caught speeding in residential area", "Traffic Violation Enforcement"),
        ("husband threatening wife during argument", "Domestic Disturbance Report"),
        ("WhatsApp account cloned and misused", "Cybercrime Report"),
        ("mentally unstable person gone missing since yesterday", "Missing Person Report"),
        
        # Environment
        ("illegal dumping of chemical waste in river", "Water Pollution"),
        ("factory emitting excessive black smoke", "Air Pollution"),
        ("loud industrial noise throughout the day", "Noise Pollution Environment"),
        ("unauthorized tree felling in protected area", "Illegal Deforestation"),
        ("improper disposal of medical waste by hospital", "Hazardous Waste Dumping"),
        ("encroachment on forest land for construction", "Forest Land Encroachment"),
        ("strong chemical odor from nearby plant impacting residents", "Industrial Emissions Impact"),
        ("plastic waste burning in open field near homes", "Open Waste Burning Health Hazard"),
        ("dead fish found in local pond, suspect contamination", "Aquatic Life Contamination"),
        ("construction debris dumped near lake shore", "Construction Debris Environmental Dumping"),
        # New entries
        ("sewage discharge into marine sanctuary", "Water Pollution"),
        ("visible particulate matter from cement factory", "Air Pollution"),
        ("24/7 generator noise from data center", "Noise Pollution Environment"),
        ("mangrove destruction for resort development", "Illegal Deforestation"),
        ("discarded batteries in municipal landfill", "Hazardous Waste Dumping"),
        ("road construction through wildlife corridor", "Forest Land Encroachment"),
        ("sulfuric acid leaks from storage tanks", "Industrial Emissions Impact"),
        ("crop residue burning affecting air quality", "Open Waste Burning Health Hazard"),
        ("oil slick observed in coastal waters", "Aquatic Life Contamination"),
        ("demolition waste dumped in green zone", "Construction Debris Environmental Dumping"),
        ("fertilizer runoff causing algal blooms", "Water Pollution"),
        ("unfiltered stack emissions from incinerator", "Air Pollution"),
        ("pile driving noise disturbing nesting birds", "Noise Pollution Environment"),
        ("pepper trees illegally cut for road widening", "Illegal Deforestation"),
        ("asbestos disposal in open pits", "Hazardous Waste Dumping"),
        ("resort construction in buffer zone", "Forest Land Encroachment"),
        ("mercury contamination near thermometer factory", "Industrial Emissions Impact"),
        ("tire burning in unauthorized recycling unit", "Open Waste Burning Health Hazard"),
        ("mass crab deaths near industrial outflow", "Aquatic Life Contamination"),
        ("concrete waste dumped in agricultural land", "Construction Debris Environmental Dumping"),
        # 37 new entries
        ("illegal dye effluents discharged into village stream", "Water Pollution"),
        ("choking smog due to unregulated factory operations", "Air Pollution"),
        ("continuous honking and loudspeakers during nighttime", "Noise Pollution Environment"),
        ("illegal chopping of trees inside eco-sensitive zone", "Illegal Deforestation"),
        ("medical syringes and waste found near public ground", "Hazardous Waste Dumping"),
        ("real estate project encroaching forest buffer zone", "Forest Land Encroachment"),
        ("chemical fumes from nearby warehouse affecting health", "Industrial Emissions Impact"),
        ("burning of plastic bags behind local market", "Open Waste Burning Health Hazard"),
        ("foul smell and fish kill in village canal", "Aquatic Life Contamination"),
        ("cement slabs and bricks dumped near riverbank", "Construction Debris Environmental Dumping"),
        ("untreated sewage released into irrigation canal", "Water Pollution"),
        ("smoke clouds from thermal plant during night hours", "Air Pollution"),
        ("generators run all night in commercial complex", "Noise Pollution Environment"),
        ("logging of trees without forest department clearance", "Illegal Deforestation"),
        ("pharmaceutical waste dumped behind clinic", "Hazardous Waste Dumping"),
        ("illegal hotel built inside forest area", "Forest Land Encroachment"),
        ("gaseous discharge causing eye irritation in colony", "Industrial Emissions Impact"),
        ("agriculture waste being burnt on open field", "Open Waste Burning Health Hazard"),
        ("frogs and turtles dying near chemical runoff zone", "Aquatic Life Contamination"),
        ("mounds of concrete rubble dumped beside road", "Construction Debris Environmental Dumping"),
        ("leakage from underground industrial drain into river", "Water Pollution"),
        ("dust clouds from cement mixing plant affecting air", "Air Pollution"),
        ("temple loudspeakers blaring from 5 AM daily", "Noise Pollution Environment"),
        ("illegal axe-cutting of trees during night", "Illegal Deforestation"),
        ("discarded paint cans and brushes near garbage dump", "Hazardous Waste Dumping"),
        ("eco-sensitive zone cleared for parking lot", "Forest Land Encroachment"),
        ("acid fumes leaking from tanker in industrial zone", "Industrial Emissions Impact"),
        ("school burning notebooks in open after exams", "Open Waste Burning Health Hazard"),
        ("fish turning belly-up in polluted backwater", "Aquatic Life Contamination"),
        ("broken tiles and bricks thrown near village pond", "Construction Debris Environmental Dumping"),
        ("polluted foam floating in drainage stream", "Water Pollution"),
        ("dense ash clouds from crematorium chimney", "Air Pollution"),
        ("concrete mixing machines running overnight", "Noise Pollution Environment"),
        ("chain-cutting of protected trees without notice", "Illegal Deforestation"),
        ("laboratory waste including vials found in canal", "Hazardous Waste Dumping"),
        ("wildlife corridor fenced off for real estate", "Forest Land Encroachment"),
        ("strong industrial solvent smell at night", "Industrial Emissions Impact"),

        # Housing and Urban Development
        # Existing 10 labels
        ("delay in allotment of government housing scheme flat", "Housing Scheme Allotment Delay"),
        ("illegal construction violating building codes next door", "Building Code Violation Report"),
        ("unsafe building structure needs inspection urgently", "Unsafe Building Inspection Request"),
        ("dispute over property boundary in urban area with neighbor", "Urban Property Boundary Dispute"),
        ("request for information on new urban development plan for our ward", "Urban Planning Information Request"),
        ("slum rehabilitation project stalled for months", "Slum Rehabilitation Project Delay"),
        ("issues with occupancy certificate for new building complex", "Occupancy Certificate Problem"),
        ("lack of basic amenities in new housing colony developed by authority", "Housing Colony Amenities Deficit"),
        ("unauthorized change of land use from residential to commercial", "Land Use Violation Report"),
        ("complaint about quality of construction in public housing project", "Public Housing Construction Quality"),

        # 8 new labels
        ("request for street lighting in newly developed residential area", "Urban Street Lighting Request"),
        ("demand for proper drainage in low-lying residential sector", "Urban Drainage Infrastructure Issue"),
        ("lack of green spaces or parks in urban housing project", "Urban Green Space Deficiency"),
        ("unauthorized encroachment on public land by vendors", "Public Land Encroachment Complaint"),
        ("rising rents due to stalled affordable housing projects", "Affordable Housing Rent Surge"),
        ("delay in approval of building plan by municipal authority", "Building Plan Approval Delay"),
        ("request for waste disposal services in high-rise society", "Waste Disposal Service Request"),
        ("complaint regarding non-functional elevators in public housing block", "Public Housing Elevator Malfunction"),
            # 47 new datasets
        ("no street lights working in new sector 12A", "Urban Street Lighting Request"),
        ("rainwater accumulates in residential area due to poor drainage", "Urban Drainage Infrastructure Issue"),
        ("no park or recreational area in the newly completed housing society", "Urban Green Space Deficiency"),
        ("vendors have occupied footpaths outside the metro station", "Public Land Encroachment Complaint"),
        ("rents have skyrocketed as affordable housing supply halted", "Affordable Housing Rent Surge"),
        ("filed building plan months ago, still no approval", "Building Plan Approval Delay"),
        ("no garbage collection in tower C for over a week", "Waste Disposal Service Request"),
        ("lift not working in government housing block G3", "Public Housing Elevator Malfunction"),
        ("neighbors constructed extra floor without permission", "Building Code Violation Report"),
        ("building beside ours has cracks, may collapse", "Unsafe Building Inspection Request"),
        ("still waiting for flat allocation under PMAY scheme", "Housing Scheme Allotment Delay"),
        ("living in slum area where rehab plan is on hold", "Slum Rehabilitation Project Delay"),
        ("our ward lacks any official development plan", "Urban Planning Information Request"),
        ("public housing flat walls are already damp and cracked", "Public Housing Construction Quality"),
        ("builder changed land use without notifying residents", "Land Use Violation Report"),
        ("builder refusing to provide occupancy certificate", "Occupancy Certificate Problem"),
        ("our block doesn't have basic water supply or drainage", "Housing Colony Amenities Deficit"),
        ("boundary wall dispute not resolved despite multiple complaints", "Urban Property Boundary Dispute"),
        ("commercial shops opened in residential complex illegally", "Land Use Violation Report"),
        ("open area behind colony turned into garbage dump", "Waste Disposal Service Request"),
        ("residents demanding public park in sector 45", "Urban Green Space Deficiency"),
        ("heavy rains caused flooding due to poor drainage", "Urban Drainage Infrastructure Issue"),
        ("we need working street lights in our alley", "Urban Street Lighting Request"),
        ("no approval for house extension from municipality", "Building Plan Approval Delay"),
        ("builders encroaching on park land for parking area", "Public Land Encroachment Complaint"),
        ("rooftop construction shaking our walls", "Building Code Violation Report"),
        ("no elevators working in high-rise EWS housing block", "Public Housing Elevator Malfunction"),
        ("housing colony roads are still kuchha after 2 years", "Housing Colony Amenities Deficit"),
        ("rent hike notices issued suddenly by private builder", "Affordable Housing Rent Surge"),
        ("we requested better lighting around housing entrance", "Urban Street Lighting Request"),
        ("low-lying house flooded every monsoon", "Urban Drainage Infrastructure Issue"),
        ("builder promised green area but gave parking instead", "Urban Green Space Deficiency"),
        ("open sewage near slum rehab towers", "Urban Drainage Infrastructure Issue"),
        ("parks near our flats are being used for storage", "Public Land Encroachment Complaint"),
        ("waiting over 8 months for building plan to be approved", "Building Plan Approval Delay"),
        ("daily complaints about broken lift go unheard", "Public Housing Elevator Malfunction"),
        ("over 200 families still waiting for housing scheme allocation", "Housing Scheme Allotment Delay"),
        ("public housing block lacks electricity backup", "Housing Colony Amenities Deficit"),
        ("builder is refusing to get OC citing technicalities", "Occupancy Certificate Problem"),
        ("neighbor’s illegal structure blocks sunlight", "Building Code Violation Report"),
        ("public land behind our house grabbed by encroachers", "Public Land Encroachment Complaint"),
        ("illegal tower built on land marked for green zone", "Land Use Violation Report"),
        ("slum rehabilitation on hold after foundation laid", "Slum Rehabilitation Project Delay"),
        ("no official communication on urban redevelopment project", "Urban Planning Information Request"),
        ("public housing units have faulty plumbing from day one", "Public Housing Construction Quality"),
        ("drainage pipes not connected in our row houses", "Urban Drainage Infrastructure Issue"),
        ("residents protested over lack of park in society", "Urban Green Space Deficiency"),
        ("unauthorized construction underway despite stop notice", "Building Code Violation Report"),

        # Social Welfare
        # Original 10 labels
        ("pension for senior citizens not received this month", "Senior Citizen Pension Disbursement"),
        ("difficulty applying for disability benefits scheme", "Disability Benefits Application Process"),
        ("scholarship for underprivileged students delayed again", "Student Scholarship Delay"),
        ("issues with anganwadi center services and timings", "Anganwadi Center Services Complaint"),
        ("need support for destitute women in our community", "Support Scheme for Destitute Women"),
        ("child labor observed in local tea shop", "Child Labor Reporting"),
        ("problems accessing old age home facilities for relative", "Old Age Home Admission Issues"),
        ("request for assistance under a specific maternal welfare scheme", "Maternal Welfare Scheme Assistance"),
        ("lack of rehabilitation services for recovered addicts in district", "Addiction Rehabilitation Services Gap"),
        ("complaint regarding midday meal quality in local school (welfare aspect)", "Midday Meal Program Quality"),

        # 8 previously added
        ("no updates on widow pension scheme application", "Widow Pension Scheme Delay"),
        ("anganwadi workers not attending regularly", "Anganwadi Staff Irregularity"),
        ("delays in issuing disability certificate", "Disability Certificate Issuance Delay"),
        ("complaint about poor hygiene at community shelter", "Community Shelter Hygiene Issue"),
        ("elderly citizens facing difficulty in availing free bus pass", "Senior Citizen Travel Concession Issue"),
        ("orphaned children not receiving government aid", "Orphan Welfare Scheme Complaint"),
        ("difficulties in availing post-natal care benefits", "Post-Natal Care Scheme Access Issue"),
        ("no vocational training options for differently-abled youth", "Vocational Training Access for Differently-Abled"),

        # 50 new labels
        ("pregnant women not receiving nutritional supplements", "Maternal Nutrition Support Issue"),
        ("no free sanitary napkins available at health center", "Sanitary Napkin Distribution Failure"),
        ("no follow-up care for malnourished children", "Child Malnutrition Follow-up Missing"),
        ("discrimination in access to welfare schemes", "Discriminatory Welfare Access"),
        ("widow denied housing under social housing scheme", "Widow Housing Scheme Denial"),
        ("manual scavengers not included in rehabilitation scheme", "Manual Scavenger Rehabilitation Gap"),
        ("children with disabilities excluded from mainstream schooling", "Inclusive Education Implementation Issue"),
        ("no ASHA worker visits in tribal hamlet", "ASHA Worker Absence"),
        ("lack of old age recreation centers in rural area", "Rural Senior Citizen Recreation Gap"),
        ("free ration card application rejected without reason", "Ration Card Application Rejection"),
        ("no creche facility for working mothers", "Creche Facility Unavailable"),
        ("shelter home overcrowded and unsafe", "Shelter Home Overcrowding"),
        ("issues in linking Aadhaar with pension account", "Aadhaar-Pension Linking Issue"),
        ("transgender individuals denied welfare benefits", "Transgender Welfare Scheme Denial"),
        ("students from SC community denied hostel seat", "Caste-based Hostel Discrimination"),
        ("street children not enrolled in any school", "Street Children Education Neglect"),
        ("no community kitchen services in flood-affected area", "Community Kitchen Service Lapse"),
        ("delay in construction of welfare housing", "Welfare Housing Project Delay"),
        ("lack of mobile health units in remote villages", "Mobile Health Unit Unavailability"),
        ("domestic violence victims not getting counseling support", "Domestic Violence Counseling Gap"),
        ("child beggars spotted at major traffic junctions", "Child Begging Reporting"),
        ("orphans not admitted to school due to lack of documents", "Orphan School Admission Issue"),
        ("delay in widow pension renewal process", "Widow Pension Renewal Delay"),
        ("unavailability of free medicines in government hospital", "Free Medicine Stock-Out"),
        ("senior citizens living alone needing urgent welfare check", "Senior Citizen Welfare Visit Request"),
        ("lack of support for mentally ill homeless individuals", "Homeless Mental Health Support Gap"),
        ("single mothers not receiving promised financial aid", "Single Mother Aid Delay"),
        ("BPL families denied subsidized LPG connection", "Subsidized LPG Access Issue"),
        ("students dropped from scholarship list without notice", "Scholarship List Exclusion Complaint"),
        ("youth from slums not included in skill training programs", "Slum Youth Skill Training Exclusion"),
        ("no enrollment drive for girl child education", "Girl Child Education Campaign Absence"),
        ("beneficiaries being charged for free scheme services", "Illegal Charges for Welfare Services"),
        ("senior citizen day care center closed without notice", "Senior Day Care Center Closure"),
        ("unhygienic conditions in government-run orphanage", "Government Orphanage Hygiene Issue"),
        ("ASHA workers demanding money for services", "ASHA Worker Corruption Report"),
        ("midday meal not being served on scheduled days", "Midday Meal Irregularity"),
        ("people with leprosy not receiving monthly assistance", "Leprosy Patient Welfare Delay"),
        ("disabled persons facing access barriers at ration shops", "Ration Shop Accessibility Issue"),
        ("health camps promised in slums never conducted", "Missing Health Camps in Slums"),
        ("manual laborers not enrolled in social security scheme", "Laborer Social Security Exclusion"),
        ("no anganwadi in newly developed colony", "Anganwadi Center Absence"),
        ("old age home lacks basic medical staff", "Old Age Home Medical Staff Shortage"),
        ("early marriage cases not being reported", "Child Marriage Reporting Lapse"),
        ("severely malnourished children not hospitalized", "Severe Malnutrition Medical Neglect"),
        ("migrant workers unaware of available welfare schemes", "Migrant Worker Welfare Awareness Gap"),
        ("free coaching centers not functioning in backward area", "Free Coaching Scheme Non-Implementation"),
        ("abandoned senior citizen not given shelter access", "Abandoned Senior Shelter Denial"),
        ("rural BPL families excluded from health insurance", "Rural Health Insurance Exclusion"),
        ("community toilets in slum area non-functional", "Community Toilet Maintenance Issue"),
        ("children denied admission in government hostels", "Government Hostel Admission Denial"),
        ("grievances regarding child adoption transparency", "Child Adoption Process Complaint"),
        ("rural girl students drop out due to lack of sanitary facilities", "Rural School Sanitation Dropout"),
        ("senior citizens not receiving winter relief kits", "Winter Relief Kit Distribution Issue"),
        ("widows facing harassment in pension distribution", "Pension Distribution Harassment"),
        
        # Public Grievances
        # Original entries (10)  
        ("delay in response from government office for RTI", "Administrative RTI Delay"),  
        ("unhelpful staff at citizen service center, rude behavior", "Government Staff Misconduct"),  
        ("corruption suspected in recent tender allocation for road work", "Corruption Allegation Tender"),  
        ("difficulty accessing public information online portal", "Public Information Access Issue"),  
        ("suggestion for improving public service delivery at Tehsil office", "Service Delivery Improvement Suggestion"),  
        ("grievance about a new traffic policy implementation without notice", "Policy Implementation Grievance"),  
        ("misleading information provided by a department official", "Misinformation by Government Official"),  
        ("no action taken on previous complaint submitted 3 months ago", "Unresolved Prior Grievance"),  
        ("problem with online portal for electricity bill payment frequently down", "Government Online Portal Outage"),  
        ("general dissatisfaction with a public office's slow functioning", "General Dissatisfaction with Public Office"),  

        # Previously added entries (6)  
        ("Unauthorized construction in residential area ignored by local authorities", "Unauthorized Construction Negligence"),  
        ("Irregular water supply in locality despite repeated complaints", "Public Utility Service Failure"),  
        ("Local government school lacking basic facilities like clean toilets", "Educational Infrastructure Deficiency"),  
        ("Excessive delay in issuing birth certificate due to system errors", "Vital Document Issuance Delay"),  
        ("Poor maintenance of public park leading to safety hazards", "Public Space Maintenance Issue"),  
        ("Unjustified hike in property tax without proper notification", "Unfair Taxation Grievance"),  

        # New entries (49)  
        ("RTI application for land records pending for 90 days", "Administrative RTI Delay"),  
        ("Municipal clerk demanded bribes to process property registration", "Government Staff Misconduct"),  
        ("Alleged favoritism in awarding contracts for school textbooks", "Corruption Allegation Tender"),  
        ("Public health data unavailable on state portal for 2 months", "Public Information Access Issue"),  
        ("Proposal to digitize land record submissions for faster service", "Service Delivery Improvement Suggestion"),  
        ("New garbage collection rules imposed without community consultation", "Policy Implementation Grievance"),  
        ("Tax officer provided incorrect deadline for filing returns", "Misinformation by Government Official"),  
        ("Complaint about blocked sewage lines unresolved for 6 weeks", "Unresolved Prior Grievance"),  
        ("Pension portal authentication failure for senior citizens", "Government Online Portal Outage"),  
        ("Frequent delays in getting appointments at district office", "General Dissatisfaction with Public Office"),  
        ("Illegal commercial setup in residential zone unreported by authorities", "Unauthorized Construction Negligence"),  
        ("Power cuts lasting 8+ hours daily in urban sector", "Public Utility Service Failure"),  
        ("Government college library closed due to structural cracks", "Educational Infrastructure Deficiency"),  
        ("Marriage certificate delayed due to misplaced paperwork", "Vital Document Issuance Delay"),  
        ("Broken benches and littered pathways in community playground", "Public Space Maintenance Issue"),  
        ("Sudden increase in business license fees without justification", "Unfair Taxation Grievance"),  
        ("No response to RTI query about municipal fund utilization", "Administrative RTI Delay"),  
        ("RTO employee shouted at applicant during license renewal", "Government Staff Misconduct"),  
        ("Bribes demanded to expedite hospital equipment procurement", "Corruption Allegation Tender"),  
        ("Missing disaster relief guidelines on district website", "Public Information Access Issue"),  
        ("Request to install biometric attendance in government offices", "Service Delivery Improvement Suggestion"),  
        ("Overnight parking ban enforced without public awareness campaign", "Policy Implementation Grievance"),  
        ("Panchayat member misinformed farmers about subsidy eligibility", "Misinformation by Government Official"),  
        ("Grievance about contaminated water supply filed 2 months ago", "Unresolved Prior Grievance"),  
        ("Agriculture subsidy portal crashed during application window", "Government Online Portal Outage"),  
        ("Excessive delays in resolving property boundary disputes", "General Dissatisfaction with Public Office"),  
        ("Illegal encroachment on public footpath ignored by corporation", "Unauthorized Construction Negligence"),  
        ("Sewage overflow in colony unresolved for 3 weeks", "Public Utility Service Failure"),  
        ("Government primary school without functional drinking water", "Educational Infrastructure Deficiency"),  
        ("Death certificate delayed due to server downtime", "Vital Document Issuance Delay"),  
        ("Public swimming pool closed indefinitely for repairs", "Public Space Maintenance Issue"),  
        ("Double taxation on rental property due to system error", "Unfair Taxation Grievance"),  
        ("Partial RTI response received after 45-day wait", "Administrative RTI Delay"),  
        ("Tehsil office staff refused to accept application without reason", "Government Staff Misconduct"),  
        ("Substandard materials used in bridge construction project", "Corruption Allegation Tender"),  
        ("Absence of pollution control board reports on official site", "Public Information Access Issue"),  
        ("Recommendation to introduce SMS alerts for application status", "Service Delivery Improvement Suggestion"),  
        ("Abrupt cancellation of subsidized LPG cylinders without notice", "Policy Implementation Grievance"),  
        ("Municipal engineer gave wrong specifications for building approval", "Misinformation by Government Official"),  
        ("Unrepaired potholes reported 4 months ago causing accidents", "Unresolved Prior Grievance"),  
        ("E-challan payment gateway non-functional for 48 hours", "Government Online Portal Outage"),  
        ("Bureaucratic delays in issuing farmer loan waivers", "General Dissatisfaction with Public Office"),  
        ("Unauthorized hoardings obstructing traffic signals", "Unauthorized Construction Negligence"),  
        ("Inconsistent garbage collection in slum areas", "Public Utility Service Failure"),  
        ("Government hostel lacks fire safety equipment", "Educational Infrastructure Deficiency"),  
        ("Delay in updating caste certificate post court order", "Vital Document Issuance Delay"),  
        ("Public amphitheater lights non-functional for months", "Public Space Maintenance Issue"),  
        ("Retroactive tax penalty imposed without prior notice", "Unfair Taxation Grievance"),  
    ]
}

def create_training_files(output_dir="training_data"):
    """
    Create properly formatted training files for Vertex AI
    """
    
    # Create main output directory
    os.makedirs(output_dir, exist_ok=True)
    
    for category, examples in training_data.items():
        # Create category directory
        category_dir = os.path.join(output_dir, category.lower().replace(" ", "_").replace("/", "_")) # Handle '/' in names
        os.makedirs(category_dir, exist_ok=True)
        
        # Create individual text files
        labels_data = []
        
        for i, (complaint_text, label) in enumerate(examples, 1):
            # Create text file
            filename = f"complaint_{i:03d}.txt"
            filepath = os.path.join(category_dir, filename)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(complaint_text)
            
            # Prepare labels data
            # Splitting 80% for TRAIN, 20% for VALIDATION. Adjust if needed.
            # For small datasets (10 examples), this means 8 train, 2 validation.
            # Vertex AI needs at least 1 for validation/test if you provide them.
            if len(examples) <= 5: # If very few examples, use all for training
                 ml_use = "TRAIN"
            elif i <= len(examples) * 0.8:
                 ml_use = "TRAIN"
            else:
                 ml_use = "VALIDATION"
            labels_data.append([ml_use, f"gs://swarajdesk-subcategory-dataset/{category.lower().replace(' ', '_').replace('/', '_')}/{filename}", label]) # Vertex AI needs GCS path
        
        # Create labels CSV file (this is one way, Vertex AI also accepts a JSONL manifest)
        # For simplicity, we'll create one CSV per category that you would then combine or use to create a manifest
        labels_file = os.path.join(category_dir, "labels.csv")
        with open(labels_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            # No header row needed if importing directly this CSV for single label text classification
            # writer.writerow(["ml_use", "gcs_file_path", "label"]) 
            for row in labels_data:
                 # Format expected by Vertex AI: GCS_FILE_PATH,label (for bulk import)
                 # Or for JSONL: {"textGcsUri": "gs://...", "classificationAnnotation": {"displayName": "label"}, "dataItemResourceLabels": {"aiplatform.googleapis.com/ml_use": "TRAIN"}}
                 f.write(f"{row[1]},{row[2]}\n") # Simplified CSV for direct import
        
        print(f"Created {len(examples)} training files for {category}")
        print(f"  Directory: {category_dir}")
        print(f"  Labels data written to: {labels_file} (format: GCS_PATH,label)")
        print(f"  Note: Update 'gs://your-bucket-name/' in labels.csv and upload files to GCS.")
        print()

def create_upload_script(bucket_name="swarajdesk-subcategory-dataset"):
    """
    Create a script to upload training data to Google Cloud Storage
    """
    
    script_content = f"""#!/bin/bash

# Target GCS bucket
BUCKET_NAME="{bucket_name}"

# Create main bucket if it doesn't exist (optional, you might create it via console)
# echo "Attempting to create bucket: $BUCKET_NAME (may fail if already exists or permissions issue)"
# gsutil mb gs://$BUCKET_NAME || echo "Bucket creation skipped or failed."

# Upload training data for each category
echo "Uploading training data..."

"""
    
    for category in training_data.keys():
        category_folder = category.lower().replace(" ", "_").replace("/", "_")
        script_content += f"""
echo "Uploading {category} data to gs://$BUCKET_NAME/{category_folder}/ ..."
gsutil -m cp -r training_data/{category_folder}/* gs://$BUCKET_NAME/{category_folder}/
"""
    
    script_content += """
echo "Upload complete!"
echo "Your training data is now available at respective folders under:"
echo "  gs://$BUCKET_NAME/"
echo ""
echo "Next steps:"
echo "1. Ensure your labels.csv files (or a combined manifest file) correctly point to these GCS locations."
echo "2. In Vertex AI, create a new Dataset, selecting 'Text' and then 'Text classification (Single-label)'."
echo "3. For import, you can point to a CSV file on GCS listing [GCS path to text file],[label] or use a JSONL manifest."
"""
    
    # Write upload script
    with open("upload_training_data.sh", "w") as f:
        f.write(script_content)
    
    # Make script executable
    os.chmod("upload_training_data.sh", 0o755)
    
    print("Created upload script: upload_training_data.sh")
    print(f"Remember to replace 'your-bucket-name' in the generated labels.csv files with '{bucket_name}' or your actual bucket name.")
    print("Run this script after installing and configuring Google Cloud SDK ('gcloud auth login', 'gcloud config set project YOUR_PROJECT_ID').")

def create_integration_example():
    """
    Create example integration code
    """
    
    integration_code = '''
from google.cloud import aiplatform
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

class ComplaintClassifier:
    def __init__(self, project_id, region="us-central1"): # Ensure region matches your Vertex AI endpoint region
        self.project_id = project_id
        self.region = region
        try:
            aiplatform.init(project=project_id, location=region)
            logging.info(f"Vertex AI initialized for project {project_id} in region {region}")
        except Exception as e:
            logging.error(f"Failed to initialize Vertex AI: {e}")
            raise
        
        # Map categories to their respective model endpoints
        # You'll need to update these with actual endpoint IDs after training and deploying models in Vertex AI
        self.endpoints = {
            "Infrastructure": "YOUR_INFRASTRUCTURE_ENDPOINT_ID", # Example: "projects/your-project-id/locations/us-central1/endpoints/1234567890"
            "Education Department": "YOUR_EDUCATION_DEPT_ENDPOINT_ID",
            "Revenue Department": "YOUR_REVENUE_DEPT_ENDPOINT_ID",
            "Health Department": "YOUR_HEALTH_DEPT_ENDPOINT_ID",
            "Water Supply and Sanitation": "YOUR_WATER_SUPPLY_ENDPOINT_ID",
            "Electricity and Power": "YOUR_ELECTRICITY_ENDPOINT_ID",
            "Transportation": "YOUR_TRANSPORTATION_ENDPOINT_ID",
            "Municipal Services": "YOUR_MUNICIPAL_SERVICES_ENDPOINT_ID",
            "Police Services": "YOUR_POLICE_SERVICES_ENDPOINT_ID",
            "Environment": "YOUR_ENVIRONMENT_ENDPOINT_ID",
            "Housing and Urban Development": "YOUR_HOUSING_ENDPOINT_ID",
            "Social Welfare": "YOUR_SOCIAL_WELFARE_ENDPOINT_ID",
            "Public Grievances": "YOUR_PUBLIC_GRIEVANCES_ENDPOINT_ID",
        }
    
    def standardize_subcategory(self, category, user_subcategory_text):
        """
        Standardize sub-category using category-specific model.
        
        Args:
            category (str): Selected category (e.g., "Infrastructure")
            user_subcategory_text (str): User input text for the sub-category (e.g., "pothole on main road")
            
        Returns:
            tuple: (standardized_subcategory, confidence_score) or (user_subcategory_text, 0.0) if error/no model
        """
        
        endpoint_id = self.endpoints.get(category)
        if not endpoint_id or endpoint_id.startswith("YOUR_"): # Check if it's a placeholder
            logging.warning(f"No deployed model endpoint ID configured for category: {category}. Returning original text.")
            return user_subcategory_text, 0.0
            
        try:
            # Construct the full endpoint name if only ID is provided, or use as is if full name.
            # Assuming endpoint_id is the numeric ID for this example.
            # For full resource name: projects/{project}/locations/{location}/endpoints/{endpoint_id}
            endpoint_path = f"projects/{self.project_id}/locations/{self.region}/endpoints/{endpoint_id}"
            endpoint = aiplatform.Endpoint(endpoint_name=endpoint_path) # Use the full path
            
            # Prepare instance for prediction. The format depends on your model's expected input.
            # For AutoML Text Classification, it's typically a list of content strings.
            instances = [{"content": user_subcategory_text}] # AutoML Text Classification expects this format
            
            logging.info(f"Sending prediction request to endpoint {endpoint_path} for category '{category}' with text: '{user_subcategory_text}'")
            prediction_response = endpoint.predict(instances=instances)
            
            logging.info(f"Raw prediction response: {prediction_response}")
            
            if not prediction_response.predictions:
                logging.error("Prediction response contained no predictions.")
                return user_subcategory_text, 0.0

            # AutoML Text Classification returns a list of predictions, one for each instance.
            # Each prediction contains 'ids', 'displayNames', 'confidences'.
            # We sent one instance, so we take the first prediction.
            result = prediction_response.predictions[0]
            
            if not result.get('displayNames') or not result.get('confidences'):
                logging.error(f"Prediction result for '{user_subcategory_text}' in category '{category}' is missing 'displayNames' or 'confidences'. Result: {result}")
                return user_subcategory_text, 0.0

            standardized_label = result['displayNames'][0] # Top prediction
            confidence = result['confidences'][0]      # Confidence of top prediction
            
            logging.info(f"Category: {category}, Input: {user_subcategory_text}")
            logging.info(f"Prediction: {standardized_label}, Confidence: {confidence:.4f}")
            
            return standardized_label, float(confidence)
            
        except Exception as e:
            logging.error(f"Error during classification for category '{category}', text '{user_subcategory_text}': {str(e)}", exc_info=True)
            return user_subcategory_text, 0.0 # Fallback to original text
    
    def process_complaint_submission(self, complaint_data):
        """
        Process complaint submission with AI standardization.
        
        Args:
            complaint_data (dict): Complaint data from user submission,
                                   expected to have 'category' and 'sub_category_text' (user's raw text).
                                   Example: {"category": "Infrastructure", "sub_category_text": "big hole in road"}
                                   
        Returns:
            dict: Enhanced complaint data with 'standardized_sub_category' and 'ai_confidence'.
        """
        
        category = complaint_data.get('category')
        user_subcategory_text = complaint_data.get('sub_category_text', '') # Assuming 'sub_category' is the raw text
        
        # Initialize AI fields
        complaint_data['standardized_sub_category'] = user_subcategory_text # Default to original
        complaint_data['ai_confidence'] = 0.0

        if not category or not user_subcategory_text:
            logging.warning("Category or sub_category_text missing, skipping AI standardization.")
            return complaint_data
        
        # Get AI standardization
        standardized, confidence = self.standardize_subcategory(category, user_subcategory_text)
        
        # Decision threshold for using AI's suggestion
        confidence_threshold = 0.70 # Adjust as needed
        
        if confidence >= confidence_threshold:
            complaint_data['standardized_sub_category'] = standardized
            complaint_data['ai_confidence'] = confidence
            logging.info(f"AI standardization applied for '{user_subcategory_text}' -> '{standardized}' with confidence {confidence:.4f}")
        else:
            # Keep original input if confidence is low or if it defaulted due to error/no model
            complaint_data['standardized_sub_category'] = user_subcategory_text # Ensure it's original if AI failed or low conf
            complaint_data['ai_confidence'] = confidence # Store the low confidence
            logging.info(f"Low confidence ({confidence:.4f}) or AI issue for '{user_subcategory_text}'. Kept original sub-category text.")
            
        return complaint_data

# --- Example Usage (Illustrative) ---
# Ensure you have GOOGLE_APPLICATION_CREDENTIALS set or are authenticated in your environment.
# Replace 'your-gcp-project-id' with your actual GCP project ID.
# Replace 'YOUR_..._ENDPOINT_ID' in the ComplaintClassifier class with actual deployed endpoint IDs.

def main_example():
    # This is where you would initialize the classifier.
    #In a real application, this might be a singleton or initialized once when the app starts.
    try:
        classifier = ComplaintClassifier(project_id="orbital-builder-454706-h5", region="us-central1") # Ensure region is correct
    except Exception as e:
        print(f"Could not initialize ComplaintClassifier: {e}")
        return

    # Example complaint data from user ( Adi Submits Complaint [cite: 130] )
    sample_complaint_1 = {
        "category": "Environment", # [cite: 130]
        "sub_category_text": "Illegal dumping of waste", # [cite: 130] Original user text for sub-category
        "description": "Illegal waste dumping in XYZ Nagar park.", # [cite: 130]
        "location": {"PIN": "400001", "City": "Mumbai", "Locality": "XYZ Nagar"}, # [cite: 131]
        "urgency": "High" # [cite: 131]
    }

    sample_complaint_2 = {
        "category": "Infrastructure",
        "sub_category_text": "pothole on main road needs fixing",
        "description": "There is a big pothole on Main Street causing traffic issues",
        "location": {"city": "Mumbai", "locality": "Andheri"},
        "urgency": "High"
    }
    
    sample_complaint_3 = {
        "category": "Health Department",
        "sub_category_text": "doctor not available in PHC", # User's raw text
        "description": "The primary health center never has a doctor during evening hours.",
        "location": {"city": "RuralTown", "locality": "Sector B"},
        "urgency": "Medium"
    }

    print("\\n--- Processing Complaint 1 (Environment) ---")
    # IMPORTANT: Ensure 'YOUR_ENVIRONMENT_ENDPOINT_ID' is replaced with a real one for this to work.
    # Otherwise, it will default to the original sub_category_text.
    enhanced_complaint_1 = classifier.process_complaint_submission(sample_complaint_1)
    print(f"Processed Complaint 1: {enhanced_complaint_1}")

    print("\\n--- Processing Complaint 2 (Infrastructure) ---")
    # IMPORTANT: Ensure 'YOUR_INFRASTRUCTURE_ENDPOINT_ID' is replaced.
    enhanced_complaint_2 = classifier.process_complaint_submission(sample_complaint_2)
    print(f"Processed Complaint 2: {enhanced_complaint_2}")
    
    print("\\n--- Processing Complaint 3 (Health Department) ---")
    # IMPORTANT: Ensure 'YOUR_HEALTH_DEPT_ENDPOINT_ID' is replaced.
    enhanced_complaint_3 = classifier.process_complaint_submission(sample_complaint_3)
    print(f"Processed Complaint 3: {enhanced_complaint_3}")
    
    # In your actual application backend (e.g., Flask, Django):
    # 1. Receive complaint data from the client.
    # 2. Get the 'category' and 'sub_category_text' (user's free-form input for sub-category).
    # 3. Call `classifier.process_complaint_submission(complaint_data)`.
    # 4. The returned `enhanced_complaint` will have:
    #    - `standardized_sub_category`: The AI's suggestion (if confidence threshold met) or the original text.
    #    - `ai_confidence`: The confidence score from the AI.
    # 5. Save this `enhanced_complaint` (including these new fields) to your database.
    #    The schema field `Complaint.Standardized_Sub_Category` would store `enhanced_complaint['standardized_sub_category']`.

if __name__ == "__main__":
    # This section will run if the script is executed directly.
    # For the integration example, you would typically call `main_example()`
    # print("Illustrative main_example for integration (requires GCP setup and deployed models):")
    # main_example() # Uncomment to run the example if you have setup your GCP env and Endpoints.
    pass # Placeholder, as the main part of the script is about generating files.

'''
    
    with open("integration_example.py", "w") as f:
        f.write(integration_code)
    
    print("Created integration example: integration_example.py")
    print("IMPORTANT: You MUST update 'YOUR_..._ENDPOINT_ID' placeholders in 'integration_example.py' with your actual Vertex AI Endpoint IDs after training and deploying your models.")
    print("Also, update 'your-gcp-project-id' in the example usage.")


if __name__ == "__main__":
    print("Generating training data files...")
    create_training_files(output_dir="training_data_all_categories") # Changed output dir to avoid conflict if old one exists
    
    print("\nCreating upload script...")
    create_upload_script(bucket_name="swarajdesk-subcategory-dataset") # Use a descriptive bucket name
    
    print("\nCreating integration example...")
    create_integration_example()
    
    print("\n--- Next steps ---")
    print("1. Review and potentially expand the 'training_data_all_categories' directory and its contents.")
    print("   Ensure the generated labels.csv files (e.g., training_data_all_categories/infrastructure/labels.csv) have the correct GCS paths after you decide on your bucket name.")
    print("   You might need to manually update 'gs://your-bucket-name/' in these CSVs to your actual bucket and path structure if you don't use 'your-complaint-classification-bucket'.")
    print("2. Make 'upload_training_data.sh' executable: chmod +x upload_training_data.sh")
    print("3. Configure Google Cloud SDK: `gcloud auth login` and `gcloud config set project YOUR_PROJECT_ID`.")
    print("4. Update the BUCKET_NAME in 'upload_training_data.sh' if different from 'your-complaint-classification-bucket'.")
    print("5. Run './upload_training_data.sh' to upload data to Google Cloud Storage.")
    print("6. In Vertex AI (Google Cloud Console):")
    print("   a. Create a new Dataset for EACH category (or one dataset with an import file referencing all categories).")
    print("      - Type: Text, Objective: Text classification (Single-label).")
    print("      - Import data from Cloud Storage, pointing to the respective category's 'labels.csv' file (e.g., gs://your-complaint-classification-bucket/infrastructure/labels.csv). Ensure this CSV contains GCS paths to .txt files and their labels.")
    print("   b. Train a new Model for EACH category using its dataset.")
    print("   c. Deploy each trained Model to an Endpoint.")
    print("   d. Note down the Endpoint ID for each deployed model.")
    print("7. Update the 'YOUR_..._ENDPOINT_ID' placeholders and 'your-gcp-project-id' in 'integration_example.py' with your actual deployed Endpoint IDs and project ID.")
    print("8. Integrate 'integration_example.py' (specifically the ComplaintClassifier class) into your complaint management system's backend to process incoming complaints.")



