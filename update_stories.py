import json

# Load existing stories
with open('stories_data.json', 'r') as f:
    data = json.load(f)

# Updates - CONSOLIDATED LIST
updates = {
    # 48. Cabinet Positions
    "48": {
        "Secretary of Agriculture": "Oversees the American farming industry, food safety, and nutrition programs like school lunches.",
        "Secretary of Commerce": "Promotes job creation and economic growth by supporting U.S. businesses and trade.",
        "Secretary of War (Defense)": "The CEO of the military. They manage the Army, Navy, Air Force, and Marines to protect national security.",
        "Secretary of Education": "Sets policies for federal financial aid for schools and collects data on America's schools.",
        "Secretary of Energy": "Manages the nation's nuclear weapons, energy research, and radioactive waste disposal.",
        "Secretary of Health and Human Services": "protects the health of all Americans and provides essential human services, including managing the CDC and FDA.",
        "Secretary of Homeland Security": "Created after 9/11, this department protects the U.S. from terrorist attacks and manages border security.",
        "Secretary of Housing and Urban Development": "Oversees federal programs designed to help Americans with their housing needs and fair housing laws.",
        "Secretary of the Interior": "Manages and conserves most federal land and natural resources, including National Parks.",
        "Secretary of Labor": "Ensures strong working conditions, advances opportunities for profitable employment, and protects benefits.",
        "Secretary of State": "The nation's top diplomat. They handle foreign affairs and relationships with other countries.",
        "Secretary of Transportation": "Ensures a fast, safe, efficient, accessible, and convenient transportation system (roads, airports, railways).",
        "Secretary of the Treasury": "Manages government revenue, prints money, and advises the President on economic policy.",
        "Secretary of Veterans Affairs": "Provides healthcare services, benefits programs, and access to national cemeteries to former military personnel.",
        "Attorney General": "The head of the Department of Justice and the chief lawyer of the federal government.",
        "Vice-President": "Ready to take over the Presidency if needed, and also casts tie-breaking votes in the Senate.",
        "Administrator of the Environmental Protection Agency": "Protects human health and the environment by enforcing regulations.",
        "Administrator of the Small Business Administration": "Supports entrepreneurs and small businesses.",
        "Director of the Central Intelligence Agency": "Gathers and analyzes national security information from around the world.",
        "Director of the Office of Management and Budget": "Produces the President's budget and measures agency performance.",
        "Director of National Intelligence": "The head of the U.S. Intelligence Community, advising the President.",
        "United States Trade Representative": "Develops and coordinates U.S. international trade policy."
    },
    
    # 51. Rights of Everyone
    "51": {
        "Freedom of expression": "You can express your ideas and opinions through art, music, or clothing without government censorship.",
        "Freedom of speech": "You can criticize the government or share unpopular opinions without fear of going to jail.",
        "Freedom of assembly": "You can gather peacefully in groups to protest or support a cause.",
        "Freedom to petition the government": "You can ask the government to fix a problem or change a law.",
        "Freedom of religion": "You can practice any religion you want, or no religion at all.",
        "The right to bear arms": "You have the right to own weapons for self-defense, as protected by the Second Amendment.",
        "Reviews laws": "Judicial Review allows courts to examine laws and actions.",
        "Explains laws": "Courts interpret what the text of a law actually means in specific cases.",
        "Resolves disputes (disagreements) about the law": "Courts settle conflicts between parties regarding legal rights.",
        "Decides if a law goes against the (U.S.) Constitution": "The power to strike down unconstitutional laws (established in Marbury v. Madison)."
    },

    # 59. State Powers
    "59": {
        "Provide schooling and education": "States manage public schools to ensure every child gets an education suited to their community.",
        "Provide protection (police)": "Local police departments are funded and managed by state and local governments to keep neighborhoods safe.",
        "Provide safety (fire departments)": "Fire and emergency services are organized locally to respond quickly to disasters.",
        "Give a driver’s license": "States issue licenses to ensure drivers know the local traffic laws.",
        "Approve zoning and land use": "Local governments decide where homes, businesses, and parks can be built."
    },

    # 65. Rights of Everyone (Specifics)
    "65": {
        "Freedom of expression": "You have the right to share your thoughts, art, and culture without censorship.",
        "Freedom of speech": "You can criticize the government or share unpopular opinions without fear of arrest.",
        "Freedom of assembly": "You can gather peacefully in groups to protest, celebrate, or support a cause.",
        "Freedom to petition the government": "You can write to officials or start petitions to ask for changes in laws.",
        "Freedom of religion": "You can practice any faith you choose, or no faith at all.",
        "The right to bear arms": "The Second Amendment protects the individual right to own weapons for self-defense."
    },

    # 67. Promises in Oath
    "67": {
        "Give up loyalty to other countries": "You promise that your sole political allegiance is now to the United States.",
        "Defend the (U.S.) Constitution": "You pledge to protect the principles and laws that define the American government.",
        "Obey the laws of the United States": "You agree to follow the rules of your new country, just like every other citizen.",
        "Serve in the military (if needed)": "If the country is at war and drafts citizens, you promise to step up.",
        "Serve (help, do important work for) the nation (if needed)": "You agree to perform civilian service during national emergencies if called upon.",
        "Be loyal to the United States": "You promise to be a faithful member of the American community."
    },

    # 69. Civic Participation
    "69": {
        "Vote": "The most powerful way to have a say in the government. Your vote decides who leads.",
        "Run for office": "You can become a leader yourself, from the local school board to the U.S. Senate.",
        "Join a political party": "You can band together with others who share your views to help get candidates elected.",
        "Help with a campaign": "Volunteering to make calls or knock on doors helps candidates connect with voters.",
        "Join a civic group": "Groups like the Rotary Club or League of Women Voters improve the community.",
        "Join a community group": "Neighborhood associations help solve local problems like safety and parks.",
        "Give an elected official your opinion (on an issue)": "Calling or writing to your representative lets them know what you care about.",
        "Contact elected officials": "They work for you! Telling them what you think is their job.",
        "Support or oppose an issue or policy": "You can attend town halls or protests to make your voice heard on specific laws.",
        "Write to a newspaper": "Letters to the editor share your opinion with the entire community."
    },

    # 73. Reasons colonists came
    "73": {
        "Freedom": "They wanted the liberty to live their lives without a King telling them what to do.",
        "Political liberty": "They wanted a say in their own government, which was impossible under the European monarchies.",
        "Religious freedom": "Many groups (like Pilgrims and Puritans) fled persecution to worship God in their own way.",
        "Economic opportunity": "The 'New World' offered land and jobs that were unavailable in the crowded cities of Europe.",
        "Practice their religion": "From Catholics in Maryland to Quakers in Pennsylvania, America became a haven for diverse faiths.",
        "Escape persecution": "People who were jailed or harassed for their beliefs in Europe found safety in the colonies."
    },

    # 77. Reasons for Declaration of Independence
    "77": {
        "High taxes": "'Taxation without Representation'! The British King taxed their tea, paper, and sugar but didn't let them have a vote in Parliament. The colonists said, 'No vote, no tax!'",
        "Taxation without representation": "'Taxation without Representation'! The British King taxed their tea, paper, and sugar but didn't let them have a vote in Parliament.",
        "British soldiers stayed in Americans’ houses (boarding, quartering)": "The 'Quartering Act' forced colonists to let British soldiers sleep in their homes and feed them! This invasion of privacy was a major reason for the revolution.",
        "They did not have self-government": "The King appointed governors who could veto any law the colonists made. They wanted to rule themselves, not be ruled by a distant island.",
        "Boston Massacre": "British soldiers shot into a crowd of protesters in Boston, killing 5 people. This violence shocked the colonies and turned opinion against the British.",
        "Boston Tea Party (Tea Act)": "Protesting the tax on tea, colonists dressed as Native Americans and dumped 342 chests of British tea into Boston Harbor.",
        "Intolerable (Coercive) Acts": "Punishment laws passed by Britain after the Tea Party, like closing Boston Harbor. These were the final straw.",
        "Stamp Act": "Required colonists to pay for a tax stamp on every piece of paper they used, from legal documents to playing cards.",
        "Sugar Act": "A tax on sugar and molasses imported into the colonies, interfering with colonial trade (especially rum).",
        "Townshend Acts": "Taxes on glass, lead, paint, paper, and tea. The colonists boycotted British goods in protest."
    },

    # 80. Revolution Events
    "80": {
        "(Battle of) Bunker Hill": "One of the first major battles. Although the British won, the Americans proved they could fight a professional army.",
        "Declaration of Independence": "Adopted on July 4, 1776, it officially announced the colonies' separation from Great Britain.",
        "Washington Crossing the Delaware (Battle of Trenton)": "A surprise attack on Christmas night 1776 that boosted American morale after a series of defeats.",
        "(Battle of) Saratoga": "The turning point of the war. This American victory convinced France to ally with the colonists.",
        "Valley Forge (Encampment)": "The winter camp where the Continental Army suffered from cold and hunger but trained to become a professional force.",
        "(Battle of) Yorktown (British surrender at Yorktown)": "The final major battle where British General Cornwallis surrendered to Washington and the French fleet."
    },
    
    # 81. 13 Original States
    "81": {
        "New Hampshire": "One of the northern colonies, known for its shipyards and fishing.",
        "Massachusetts": "Home to Boston, the Tea Party, and the first battles of the Revolution at Lexington and Concord.",
        "Rhode Island": "Where the first calls for independence began; heavily involved in maritime trade.",
        "Connecticut": "Known as the 'Provision State' for supplying food and cannons to the Continental Army.",
        "New York": "Strategically vital; the British occupied New York City for most of the war.",
        "New Jersey": "Called the 'Crossroads of the Revolution' because more battles were fought here than in any other state.",
        "Pennsylvania": "Home to Philadelphia, where the Declaration of Independence and Constitution were written.",
        "Delaware": "The 'First State' to ratify the Constitution.",
        "Maryland": "Specifically founded as a haven for Catholics effectively establishing religious tolerance.",
        "Virginia": "The largest and wealthiest colony; home to Washington, Jefferson, and Madison.",
        "North Carolina": "The first colony to officially authorize its delegates to vote for independence.",
        "South Carolina": "Suffered more battles and skirmishes in the later years of the war than almost any other state.",
        "Georgia": "The southernmost colony; the last to join the rebellion and the first to be reconquered by the British."
    },

     # 83. Federalist Writers
    "83": {
        "(Alexander) Hamilton": "He wrote the majority of the essays (51 of 85), focusing on the defects of the confederation and strong executive power.",
        "(James) Madison": "He wrote about the checks and balances and the separation of powers (famous Essay #10 and #51).",
        "(John) Jay": "He wrote 5 essays focusing on foreign relations before becoming ill.",
        "Publius": "The pen name used by all three men to keep their identities secret while encouraging ratification."
    },
    
    # 84. Importance of Federalist Papers
    "84": {
        "They helped people understand the (U.S.) Constitution.": "They explained exactly how the new government would work to reducing fears of a new tyranny.",
        "They supported passing the (U.S.) Constitution.": "They were written to convince the voters of New York to ratify the new Constitution."
    },

    # 85. Franklin
    "85": {
        "Founded the first free public libraries": "He believed education should be available to everyone, not just the rich.",
        "First Postmaster General of the United States": "He improved the mail system, making communication between the colonies faster and more reliable.",
        "Helped write the Declaration of Independence": "The oldest member of the committee, he edited Jefferson's draft to ensure it appealed to all.",
        "Inventor": "He invented the lightning rod, bifocals, and the Franklin stove.",
        "U.S. diplomat": "He went to France and convinced them to support the American Revolution with money and troops."
    },

    # 86. Washington
    "86": {
        "Father of Our Country": "A title given to him because his leadership was essential for the birth and survival of the nation.",
        "First president of the United States": "He set the standard for the presidency, serving two terms and then peacefully stepping down.",
        "General of the Continental Army": "He led the colonial forces against the British Empire, holding the army together through freezing winters.",
        "President of the Constitutional Convention": "He presided over the drafting of the Constitution, lending his immense prestige to the new government."
    },
    
    # 87. Jefferson
    "87": {
        "Writer of the Declaration of Independence": "At age 33, he wrote the document that declared the U.S. free from Britain and stated that 'all men are created equal'.",
        "Third president of the United States": "He served two terms from 1801 to 1809, emphasizing a smaller government and agrarian democracy.",
        "Doubled the size of the United States (Louisiana Purchase)": "In 1803, he bought a massive chunk of land from France for $15 million, extending the U.S. to the Rocky Mountains.",
        "First Secretary of State": "He served as the very first top diplomat under George Washington.",
        "Founded the University of Virginia": "He was so proud of this that he put it on his tombstone instead of being President!",
        "Member of the Continental Congress": "He represented Virginia and helped draft the Articles of Confederation and the Declaration."
    },

     # 88. Madison
    "88": {
        "Father of the Constitution": "He arrived at the convention with the detailed plan that became the framework of our government.",
        "Fourth president of the United States": "He served after Jefferson and led the nation through the War of 1812.",
        "President during the War of 1812": "He was the first president to ask Congress to declare war (against Britain).",
        "One of the writers of the Federalist Papers": "He wrote 29 of the 85 essays, arguing brilliantly for a strong federal government."
    },

    # 89. Hamilton
    "89": {
        "First Secretary of the Treasury": "He created the financial system of the U.S., including the Mint and the first National Bank.",
        "One of the writers of the Federalist Papers": "He wrote the majority of the essays (51 of 85!), defending the new Constitution.",
        "Helped establish the First Bank of the United States": "He believed a central bank was necessary to stabilize the young nation's economy.",
        "Aide to General George Washington": "During the war, he was Washington's right-hand man and trusted advisor.",
        "Member of the Continental Congress": "He represented New York and was a vocal advocate for a stronger union of states."
    },

    # 90. Louisiana Purchase
    "90": {
        "Louisiana Territory": "The massive region from the Mississippi River to the Rockies.",
        "Louisiana": "The purchase was named after this territory, though it covers much more than the modern state."
    },
    
    # 91. 1800s Wars
    "91": {
        "War of 1812": "Fought against Britain over trade restrictions and the impressment of American sailors.",
        "Mexican-American War": "Fought from 1846-1848, resulting in the U.S. gaining California, Arizona, New Mexico, and more.",
        "Civil War": "The bloody conflict (1861-1865) between the North and South over slavery and states' rights.",
        "Spanish-American War": "Fought in 1898, leading to the U.S. acquiring Puerto Rico, Guam, and the Philippines."
    },

    # 92. Problems leading to Civil War
    "92": {
        "Slavery": "The South wanted to keep slavery for their plantation economy, while the North largely opposed its expansion.",
        "Economic reasons": "The industrial North and agricultural South had very different economic needs and disagreed on tariffs.",
        "States’ rights": "Southern states argued they had the right to ignore federal laws they didn't like, including potential bans on slavery."
    },

    # 93. Civil War Events
    "93": {
        "(Battle of) Fort Sumter": "The first shots of the Civil War were fired here in South Carolina in 1861.",
        "Emancipation Proclamation": "Lincoln's executive order that declared slaves in the rebelling states to be free.",
        "(Battle of) Vicksburg": "A key Union victory that gave the North control of the Mississippi River, splitting the Confederacy.",
        "(Battle of) Gettysburg": "The bloodiest battle of the war and a turning point that stopped the South's invasion of the North.",
        "Sherman’s March": "A destructive campaign through Georgia that demoralized the South and hastened the end of the war.",
        "(Surrender at) Appomattox": "Where General Lee surrendered to General Grant in 1865, effectively ending the war.",
        "(Battle of) Antietam/Sharpsburg": "The deadliest single-day battle in American history.",
        "Lincoln was assassinated.": "Just days after the war ended, John Wilkes Booth killed the President at Ford's Theatre."
    },

    # 94. Lincoln
    "94": {
        "Freed the slaves (Emancipation Proclamation)": "He signed the order that began the legal end of slavery in the U.S.",
        "Saved (or preserved) the Union": "He refused to let the country break apart, fighting to keep the United States united.",
        "Led the United States during the Civil War": "He was the Commander-in-Chief during the deadliest conflict in American history.",
        "16th president of the United States": "He was the first Republican president, elected in 1860.",
        "Delivered the Gettysburg Address": "A short but powerful speech honoring the fallen soldiers and redefining the war as a fight for human equality."
    },
    
    # 95. Emancipation Proclamation
    "95": {
        "Freed the slaves": "It declared that all persons held as slaves in the rebellious states are, and henceforward shall be free.",
        "Freed slaves in the Confederacy": "It specifically targeted the Southern states fighting against the Union.",
        "Freed slaves in the Confederate states": "It turned the Civil War from a fight about Union into a fight for human freedom.",
        "Freed slaves in most Southern states": "It applied to states in rebellion, exempting loyal border states initially."
    },

    # 98. Right to Vote (Men)
    "98": {
        "After the Civil War": "The end of slavery brought the push for black male suffrage.",
        "During Reconstruction": "The period after the war when the federal government enforced rights in the South.",
        "(With the) 15th Amendment": "Ratified in 1870, ensuring race could not be used to deny the vote.",
        "1870": "The year the 15th Amendment was officially added to the Constitution."
    },

    # 99. Women's Rights Leaders
    "99": {
        "Susan B. Anthony": "She was arrested for voting illegally in 1872! She appeared on the dollar coin and spent her life fighting for suffrage.",
        "Elizabeth Cady Stanton": "She organized the Seneca Falls Convention in 1848 and wrote the 'Declaration of Sentiments', demanding equality.",
        "Sojourner Truth": "A former slave who became a powerful speaker. Her famous 'Ain't I a Woman?' speech linked women's rights with abolition.",
        "Harriet Tubman": "Famous for the Underground Railroad, she was also a suffragist who fought for women's right to vote after the Civil War.",
        "Lucretia Mott": "A Quaker abolitionist and women's rights activist who helped organize the Seneca Falls Convention.",
        "Lucy Stone": "She was the first woman in Massachusetts to earn a college degree and kept her maiden name after marriage as a protest."
    },

    # 100. Wars in 1900s
    "100": {
        "World War I": "The 'Great War' (1914-1918). The U.S. joined in 1917 to help the Allies defeat the Central Powers.",
        "World War II": "The biggest war in history (1939-1945). The U.S. fought Nazi Germany in Europe and Imperial Japan in the Pacific.",
        "Korean War": "Fought in the early 1950s to stop communist North Korea from taking over South Korea. It ended in a stalemate.",
        "Vietnam War": "A long conflict (1955-1975) to stop the spread of communism in Vietnam. It was highly controversial in the U.S.",
        "Persian Gulf War": "Fought in 1991 (Operation Desert Storm) to liberate Kuwait after it was invaded by Iraq's Saddam Hussein."
    },
    
    # 101. WWI Reasons
    "101": {
        "Because Germany attacked U.S. (civilian) ships": "German U-boats sank American merchant ships (like the Lusitania), killing innocent civilians.",
        "To support the Allied Powers (England, France, Italy, and Russia)": "We shared democratic values and economic ties with the Allies, and had loaned them massive amounts of money.",
        "To oppose the Central Powers (Germany, Austria-Hungary, the Ottoman Empire, and Bulgaria)": "Germany's aggression and the Zimmerman Telegram (plotting with Mexico) were seen as direct threats."
    },

     # 106. WWII Reasons
    "106": {
        "(Bombing of) Pearl Harbor": "Japan's surprise attack on the U.S. Pacific Fleet in Hawaii killed 2,403 Americans and thrust the U.S. into the war.",
        "Japanese attacked Pearl Harbor": "On December 7, 1941, 'a date which will live in infamy', Japan struck without warning.",
        "To support the Allied Powers (England, France, and Russia)": "The U.S. became the 'Arsenal of Democracy', sending supplies before officially joining the fight.",
        "To oppose the Axis Powers (Germany, Italy, and Japan)": "These fascist regimes sought global conquest and committed horrific atrocities (Holocaust, Nanking)."
    },
    
    # 107. Eisenhower
    "107": {
        "General during World War II": "He was the Supreme Commander of Allied Forces in Europe, leading D-Day.",
        "President at the end of (during) the Korean War": "He negotiated the armistice that stopped the fighting in Korea.",
        "34 th president of the United States": "He signed the act creating the Interstate Highway System."
    },

    # 108. Cold War Rival
    "108": {
        "Soviet Union": "The communist superpower that competed with the U.S. for global influence.",
        "USSR": "The Union of Soviet Socialist Republics, which dissolved in 1991.",
        "Russia": "The largest republic within the Soviet Union, often used as a synonym."
    },

    # 109. Cold War Concern
    "109": {
        "Communism": "An economic and political system where the state owns all property, which the U.S. opposed.",
        "Nuclear war": "The fear that conflict between superpowers could destroy the world with atomic weapons."
    },

    # 113. MLK
    "113": {
        "Fought for civil rights": "He led nonviolent protests to end segregation and racial injustice in America.",
        "Worked for equality for all Americans": "He dreamed of a nation where people would be judged by their character, not their skin color.",
        "Worked to ensure that people would “not be judged by the color of their skin, but by the content of their character”": "A famous quote from his 'I Have a Dream' speech at the March on Washington."
    },

    # 115. 9/11 Events
    "115": {
        "Terrorists attacked the United States": "The deadliest terrorist act in world history, orchestrated by Al-Qaeda.",
        "Terrorists took over two planes and crashed them into the World Trade Center in New York City": "The Twin Towers collapsed, forever changing the New York skyline and American sense of security.",
        "Terrorists took over a plane and crashed into the Pentagon in Arlington, Virginia": "The attack partially destroyed the headquarters of the U.S. Department of Defense.",
        "Terrorists took over a plane originally aimed at Washington, D.C., and crashed in a field in Pennsylvania": "Passengers on Flight 93 fought back, sacrificing themselves to save the Capitol or White House."
    },
    
    # 116. Post-9/11 Conflicts
    "116": {
        "War in Afghanistan": "Launched to dismantle Al-Qaeda and remove the Taliban regime that harbored them.",
        "War in Iraq": "Launched based on intelligence that Saddam Hussein possessed weapons of mass destruction (WMDs).",
        "(Global) War on Terror": "A broad military and legal campaign to fight extremist organizations worldwide."
    },
    
    # 117. Tribes
    "117": {
         "Cherokee": "Originally from the Southeast; forced to relocate on the Trail of Tears.",
         "Navajo": "The largest tribe today, known for their shepherds, weavers, and Code Talkers.",
         "Sioux": "Great Plains tribe (Lakota/Dakota) who followed the buffalo and fought at Little Bighorn.",
         "Chippewa": "Also known as Ojibwe, they lived around the Great Lakes and harvested wild rice.",
         "Choctaw": "One of the 'Five Civilized Tribes' from the Southeast, known for their code talkers in WWI.",
         "Pueblo": "Southwestern people known for their multi-story adobe buildings and pottery.",
         "Apache": "Nomadic hunters and warriors of the Southwest; fiercely resisted reservation life.",
         "Iroquois": "A powerful confederacy in the Northeast with a sophisticated democratic government.",
         "Creek": "Muscogee people from the Southeast; many were forced to Oklahoma.",
         "Blackfeet": "Powerflul Plains tribe of Montana, known for their horsemanship.",
         "Seminole": "Based in Florida, they fought three wars against the U.S. and never signed a peace treaty.",
         "Cheyenne": "Plains tribe that allied with the Sioux; suffered the Sand Creek Massacre.",
         "Arawak": "Indigenous people of the Caribbean encountered by Columbus.",
         "Shawnee": "Led by the famous Tecumseh, they fought to unite tribes against expansion.",
         "Mohegan": "Algonquian people of Connecticut, allies of the English in early wars.",
         "Huron": "Allies of the French in the Northeast fur trade.",
         "Oneida": "One of the Iroquois nations; the only one to side with the Americans in the Revolution.",
         "Lakota": "A major division of the Sioux; known for Sitting Bull and Wounded Knee.",
         "Crow": "Plains tribe that often served as scouts for the U.S. Army.",
         "Teton": "Another name for the Lakota Sioux.",
         "Hopi": "Southwestern 'Peaceful Ones' known for living on high mesas.",
         "Inuit": "Indigenous people of the Arctic (Alaska) adapted to the extreme cold.",
         "Inupiat": "Native Alaskans known for hunting whales and living in the far north.",
         "Mohawk": "Keepers of the Eastern Door of the Iroquois Confederacy; expert ironworkers.",
         "Onondaga": "Keepers of the Central Council Fire of the Iroquois Confederacy.",
         "Seneca": "Keepers of the Western Door of the Iroquois Confederacy.",
         "Tuscarora": "A southern tribe that joined the Iroquois Confederacy in the 1700s.",
         "Tuscarora For a complete list of tribes, please visit bia.gov.": "A southern tribe that joined the Iroquois Confederacy in the 1700s.",
        # Catch-alls
        "DEFAULT": "One of the sovereign tribal nations indigenous to North America."
    },

    # 118. Innovations
    "118": {
        "Light bulb": "Thomas Edison's invention extended the day, changing how we live and work forever.",
        "Automobile (cars, internal combustion engine)": "Henry Ford's assembly line made cars affordable, transforming American travel and cities.",
        "Skyscrapers": "Steel frames and elevators allowed cities to grow upwards, creating the modern skyline.",
        "Airplane": "The Wright Brothers achieved the first powered flight, shrinking the world and revolutionizing travel.",
        "Assembly line": "Ransom Olds and Henry Ford perfected mass production, making goods cheaper and raising the standard of living.",
        "Landing on the moon": "The Apollo 11 mission proved American technological dominance and fulfilled Kennedy's promise.",
        "Integrated circuit (IC)": "The microchip makes all modern electronics (computers, phones, the internet) possible."
    },
    
    # 12. Rule of Law (Previously 12, now explicitly re-added below as 13 if needed, but wait)
    # The snippet had "12" then "13". I'll put exact content.
    
    # 12. Economic System (Correct ID)
    "12": {
        "Capitalism": "An economic system where private individuals own businesses and compete for profit.",
        "Free market economy": "A system where prices are determined by supply and demand with little government control."
    },

    # 14. Influential Documents
    "14": {
        "Declaration of Independence": "It established the ideals of equality and natural rights that are the foundation of the Constitution.",
        "Articles of Confederation": "The first U.S. constitution; its failure showed the need for a stronger federal government.",
        "Federalist Papers": "These essays explained the reasoning behind the Constitution's design and remain a primary source for interpretation.",
        "Anti-Federalist Papers": "These arguments highlighted fears of central power, leading directly to the adoption of the Bill of Rights.",
        "Virginia Declaration of Rights": "Written by George Mason, it served as a model for the Bill of Rights.",
        "Fundamental Orders of Connecticut": "Often called the first written constitution in America, establishing a representative government.",
        "Mayflower Compact": "The first agreement for self-government in America, signed by the Pilgrims in 1620.",
        "Iroquois Great Law of Peace": "The oral constitution of the Iroquois Confederacy, which some say inspired the U.S. federal system."
    },

    # 15. Three Branches Reason
    "15": {
        "Checks and balances": "Each branch has the power to limit the actions of the other two, ensuring cooperation.",
        "Separation of powers": "Dividing authority prevents any single group from gaining total control."
    },

    # 16. Three Branches
    "16": {
        "Legislative, executive, and judicial": "These correspond to the Congress (making laws), President (enforcing laws), and Courts (judging laws).",
        "Congress, president, and the courts": "The three distinct arms of the federal government interacting to govern the nation."
    },

    # 18. Who writes laws
    "18": {
        "(U.S.) Congress": "The national legislative body consisting of the House and Senate.",
        "(U.S. or national) legislature": "The formal law-making assembly of the federal government.",
        "Legislative branch": "The branch empowered by Article I of the Constitution to create federal statutes."
    },

    # 20. Congress Powers
    "20": {
        "Writes laws": "The primary duty of Congress is to draft, debate, and pass legislation.",
        "Declares war": "By the Constitution, only Congress can officially declare war, not the President.",
        "Makes the federal budget": "Congress controls the 'power of the purse', deciding how government money is collected and spent."
    },

    # 28. Senators per state
    "28": {
        "Equal representation (for small states)": "This ensures that small states like Delaware have the same voice in the Senate as large states like California.",
        "The Great Compromise (Connecticut Compromise)": "The agreement that created a bicameral legislature, blending representation by population and by state equality."
    },

    # 31. Who Senator Represents
    "31": {
        "Citizens of their state": "Senators are elected to serve the interests of the entire state.",
        "People of their state": "Unlike House members who represent a district, Senators represent all residents of their state."
    },

    # 33. Who Rep Represents
    "33": {
        "Citizens in their (congressional) district": "Representatives serve specific geographic areas within a state.",
        "People from their (congressional) district": "They are the most local voice in the federal government.",
        "People in their district": "Roughly 700,000 to 800,000 distinct constituents per representative."
    },

    # 35. More Reps
    "35": {
        "(Because of) the state’s population": "States with more people need more representatives to ensure equal representation for citizens.",
        "(Because) they have more people": "California has 52 reps (huge population), while Wyoming has only 1 (small population).",
        "(Because) some states have more people": "Representation in the House is based on the census count every 10 years."
    },

    # 37. Two Terms
    "37": {
        "(Because of) the 22nd Amendment": "Passed after FDR served four terms, making the two-term tradition a formal law.",
        "To keep the president from becoming too powerful": "Regular rotation in office prevents tyranny and brings fresh leadership."
    },

    # 41. Powers of President
    "41": {
        "Signs bills into law": "The President's signature is the final step in making a bill a law.",
        "Vetoes bills": "The President can reject a bill passed by Congress (though Congress can override it).",
        "Enforces laws": "The Executive branch is responsible for carrying out and administering federal laws.",
        "Commander in Chief (of the military)": "The President has final authority over all U.S. military operations.",
        "Chief diplomat": "The President directs foreign policy and negotiates with other nations.",
        "Appoints federal judges": "The President nominates judges to the Supreme Court and lower courts."
    },

    # 46. Executive Branch Parts
    "46": {
        "President (of the United States)": "The head of the branch and the state.",
        "Cabinet": "The advisors who lead the 15 executive departments.",
        "Federal departments and agencies": "The massive organizations (like the FBI, FDA, EPA) that do the daily work of government."
    },
    
    # 49. Electoral College
    "49": {
        "It decides who is elected president.": "The formal body that elects the President and Vice President.",
        "It provides a compromise between the popular election of the president and congressional selection.": "The founders created it to balance the interests of large and small states."
    },

    # 50. Judicial Branch Parts
    "50": {
        "Supreme Court": "The highest court in the land, its decisions are final.",
        "Federal Courts": "The system of district and appellate courts that handle federal cases below the Supreme Court."
    },

    # 51. Judicial Branch Job
    "51": {
        "Reviews laws": "Judicial Review allows courts to examine laws and actions.",
        "Explains laws": "Courts interpret what the text of a law actually means in specific cases.",
        "Resolves disputes (disagreements) about the law": "Courts settle conflicts between parties regarding legal rights.",
        "Decides if a law goes against the (U.S.) Constitution": "The power to strike down unconstitutional laws (established in Marbury v. Madison)."
    },

    # 55. Justices Term
    "55": {
        "(For) life": "Justices serve until they die, retire, or are impeached.",
        "Lifetime appointment": "Ensures they don't have to worry about reelection.",
        "(Until) retirement": "They can choose to step down when they wish."
    },

    # 56. Why Life Term
    "56": {
        "To be independent (of politics)": "They shouldn't be swayed by public opinion or voters.",
        "To limit outside (political) influence": "They answer only to the Constitution and the law, not to a political party."
    },

    # 58. Federal Powers
    "58": {
        "Print paper money": "Only the federal government can issue currency to ensure a stable economy.",
        "Mint coins": "Coinage is an exclusive federal power to prevent confusion.",
        "Declare war": "A sovereign power reserved for the national government.",
        "Create an army": "To provide for the common defense of the entire nation.",
        "Make treaties": "Relationships with other nations are handled as one united country.",
        "Set foreign policy": "The U.S. speaks with one voice on the international stage."
    },

    # 70. Serve Country
    "70": {
        "Vote": "Participating in elections dictates the direction of the country.",
        "Pay taxes": "Funding the government ensures services like defense and infrastructure act.",
        "Obey the law": "A peaceful society depends on citizens following the rules.",
        "Serve in the military": "Defending the nation is one of the highest forms of service.",
        "Run for office": "Taking a leadership role to serve the public directly.",
        "Work for local, state, or federal government": "Civil servants keep the government running every day."
    },

    # 71. Pay Taxes
    "71": {
        "Required by law": "Tax evasion is a crime; everyone must contribute their share.",
        "All people pay to fund the federal government": "Taxes pay for the military, highways, and social programs.",
        "Required by the (U.S.) Constitution (16th Amendment)": "The 16th Amendment specifically authorizes Congress to levy an income tax.",
        "Civic duty": "Contributing to the common good is a responsibility of citizenship."
    },

    # 72. Selective Service
    "72": {
        "Required by law": "Almost all male citizens and immigrants aged 18-25 must register.",
        "Civic duty": "Being ready to defend the nation in a crisis is a responsibility.",
        "Makes the draft fair, if needed": "If a draft were reinstated, the lottery would be based on this registration list."
    },

    # 74. Pre-European
    "74": {
        "American Indians": "The indigenous peoples who have lived here for thousands of years.",
        "Native Americans": "The original inhabitants of the North American continent."
    },

    # 75. Slaves
    "75": {
        "Africans": "Millions were forcibly taken from the African continent.",
        "People from Africa": "Enslaved people were kidnapped and transported across the Atlantic."
    },

    # 76. War for Independence
    "76": {
        "American Revolution": "The upheaval that birthed the United States.",
        "The (American) Revolutionary War": "The military conflict between the colonies and Great Britain (1775-1783).",
        "War for (American) Independence": "The struggle to become a sovereign nation."
    },

    # 102. Women Vote
    "102": {
        "1920": "The year the 19th Amendment was ratified.",
        "After World War I": "Women's contributions during the war helped build support for suffrage.",
        "(With the) 19 th Amendment": "The constitutional change that guaranteed women the right to vote."
    },

    # 120. Statue of Liberty
    "120": {
        "New York (Harbor)": "She stands on Liberty Island, greeting ships entering New York City.",
        "Liberty Island [Also acceptable are New Jersey, near New York City, and on the Hudson (River).]": "The federal island where the statue stands, technically in New Jersey waters but part of NY."
    },

    # 121. 13 Stripes
    "121": {
        "(Because there were) 13 original colonies": "The first 13 states that declared independence.",
        "(Because the stripes) represent the original colonies": "They remind us of our history and the original union."
    },

    # 122. 50 Stars
    "122": {
        "(Because there is) one star for each state": "As the country grows, we add a star.",
        "(Because) each star represents a state": "Each state is equal in the union, represented by a single star.",
        "(Because there are) 50 states": "The current number of states in the Union, from Alabama to Wyoming."
    },

    # 124. E Pluribus Unum
    "124": {
        "Out of many, one": "From many different colonies and people, one single united nation was formed.",
        "We all become one": "A poetic way to say we are united as one people despite our differences."
    },

    # 125. Independence Day
    "125": {
        "July 4": "The specific date on the calendar we celebrate.",
        "The country’s birthday": "The day the U.S. was 'born' by declaring itself free.",
        "A holiday to celebrate U.S. independence (from Britain)": "The official reason for the holiday."
    },

    # 126. Holidays
    "126": {
        "Thanksgiving Day": "Commemorates the 1621 feast between Pilgrims and Wampanoag people.",
        "Christmas Day": "A Christian holiday celebrating the birth of Jesus, also a cultural holiday.",
        "Presidents Day (Washington’s Birthday)": "Honors the birthdays of Washington and Lincoln, and all past presidents.",
        "Martin Luther King, Jr. Day": "Honors the civil rights leader's birthday and commitment to nonviolent change.",
        "Memorial Day": "Honors soldiers who died in war (May).",
        "Veterans Day": "Honors all who served in the military (November).",
        "New Year’s Day": "Celebrated on January 1st to mark the beginning of the new Gregorian calendar year.",
        "Juneteenth": "Celebrated on June 19th to commemorate the end of slavery in the U.S.",
        "Independence Day": "July 4th! The anniversary of the publication of the Declaration of Independence in 1776.",
        "Labor Day": "Celebrated in September to honor the American labor movement.",
        "Columbus Day": "Commemorates the landing of Christopher Columbus in the Americas in 1492."
    },
    
    # 128. Veterans Day
    "128": {
        "A holiday to honor people in the (U.S.) military": "Recognizing those currently serving.",
        "A holiday to honor people who have served (in the U.S. military)": "Specifically honoring those who have completed their service."
    },

    # 1. Form of Government
    "1": {
        "Republic": "In a republic, the people hold power but elect representatives to exercise it, rather than having a monarch.",
        "Constitution-based federal republic": "Our government operates under the supreme law of the Constitution, with power shared between national and state levels.",
        "Representative democracy": "Citizens vote for officials who make laws and decisions on their behalf."
    },
    
    # 3. Constitution Function
    "3": {
        "Forms the government": "It created the three branches (Legislative, Executive, Judicial) and the structure of federal power.",
        "Defines powers of government": "It lists exactly what the federal government can and cannot do (like declaring war or coining money).",
        "Defines the parts of government": "It outlines the duties of the Congress, President, and Supreme Court.",
        "Protects the rights of the people": "Through the Bill of Rights, it guarantees freedoms that the government cannot take away."
    },
    
    # 4. We the People
    "4": {
        "Self-government": "The idea that the people are the ultimate source of political power.",
        "Popular sovereignty": "The belief that the authority of the state is created and sustained by the consent of its people.",
        "Consent of the governed": "The government only serves because the people agree to it.",
        "People should govern themselves": "We do not answer to a King; we dictate our own future.",
        "(Example of) social contract": "An agreement among the members of a society to cooperate for social benefits."
    },
    
    # 5. Changes to Constitution
    "5": {
        "Amendments": "Changes or additions to the text of the Constitution.",
        "The amendment process": "The formal method listed in Article V for proposing and ratifying changes."
    },
    
    # 6. Bill of Rights
    "6": {
        "The basic rights of people living in the United States": "Fundamental freedoms like speech and religion that belong to everyone.",
        "Protects the rights of the people": "It ensures the government cannot infringe on individual liberties.",
        "(The basic) rights of Americans": "The core privileges that define lawful residence in the U.S.",
        "(The basic) rights of people living in the United States": "It covers everyone on U.S. soil, not just citizens."
    },
    
    # 8. Declaration Purpose
    "8": {
        "Announced our independence (from Great Britain)": "A public statement to the world that the 13 colonies were leaving the British Empire.",
        "Declared our independence (from Great Britain)": "The formal legal assertion that the political bands with Britain were cut.",
        "Said that the United States is free (from Great Britain)": "It proclaimed the birth of a new, sovereign nation.",
        "It says all people are created equal.": "The philosophical core of the document, stating that human rights are inherent.",
        "It identifies inherent rights.": "It claims rights come from 'Nature and Nature's God', not the King.",
        "It identifies individual freedoms.": "Life, Liberty, and the pursuit of Happiness are mentioned specifically."
    },
    
    # 10. Declaration/Constitution Ideas
    "10": {
        "Liberty": "The freedom to live your life as you choose within the law.",
        "Equality": "The belief that no person is superior to another by birth.",
        "Natural rights": "Rights that human beings have by their nature, not by government gift.",
        "Limited government": "The government is not all-powerful and may only do those things the people have given it the power to do.",
        "Self-government": "Citizens have a direct say in how they are governed.",
        "Rule of law": "The principle that law governs a nation, as opposed to an individual official."
    },
    
    # 13. Rule of Law (Corrected from ID 12)
    "13": {
        "Everyone must follow the law.": "No individual is exempt, regardless of their status or power.",
        "Leaders must obey the law.": "Those who make and enforce the laws are also subject to them.",
        "Government must obey the law.": "The state itself cannot act arbitrarily; it is bound by the constitution and statutes.",
        "No one is above the law.": "The core principle that ensures equality and justice for all citizens."
    },
    
    # 63. Voting Amendments
    "63": {
        "Citizens eighteen (18) and older (can vote).": "The 26th Amendment lowered the voting age from 21 to 18.",
        "You don’t have to pay (a poll tax) to vote.": "The 24th Amendment banned poll taxes, which had been used to stop poor people from voting.",
        "Any citizen can vote. (Women and men can vote.)": "The 19th Amendment guaranteed women the right to vote.",
        "A male citizen of any race (can vote).": "The 15th Amendment prevented the denial of the vote based on race."
    },
    
    # 64. Who can vote
    "64": {
        "Citizens of the United States": "Only fully naturalized or native-born citizens have the full franchise in federal elections.",
        "Citizens": "Voting is one of the key rights reserved specifically for members of the polity.",
        "U.S. citizens": "Non-residents and green card holders cannot vote in federal elections."
    },
    
    # 66. Pledge Loyalty
    "66": {
        "The United States": "You are pledging allegiance to the nation itself.",
        "The flag": "The flag serves as the symbol of the country and its values."
    },
    
    # 68. Citizenship
    "68": {
        "Naturalize": "The legal process by which a non-citizen acquires citizenship.",
        "Derive citizenship (under conditions set by Congress)": "Children often become citizens automatically when their parents naturalize.",
        "Be born in the United States, under the conditions set by the 14th Amendment": "Birthright citizenship ensures everyone born on U.S. soil is a citizen."
    }
}

# Apply updates (merge)
for q_id, answers in updates.items():
    if q_id in data:
        # We need to keep the old DEFAULT if we want, or just overwrite the ID entry with new map
        # But wait, existing entries are just { "DEFAULT": "..." }
        # We want to keep DEFAULT as a fallback if not provided in 'answers' dict above?
        # The 'answers' dict above has specific keys.
        
        # Let's ensure there is a DEFAULT in the new map, maybe from the old map
        old_default = data[q_id].get("DEFAULT", "")
        
        # Start with the new specific answers
        new_entry = answers.copy()
        
        # If the new entry doesn't have a DEFAULT, use the old one
        if "DEFAULT" not in new_entry:
            new_entry["DEFAULT"] = old_default
            
        data[q_id] = new_entry
    else:
        print(f"Warning: Question ID {q_id} not found in original data.")

# Write back
with open('stories_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Updated stories_data.json with specific answers.")
