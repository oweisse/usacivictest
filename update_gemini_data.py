import json
import os

FILE_PATH = 'gemini_data.json'

def update_data():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'r') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = {}
    else:
        data = {}

    # Batch 6: Questions 101-128
    new_data = {
        "101": {
            "Because Germany attacked U.S. (civilian) ships": "Unrestricted submarine warfare, including the sinking of the Lusitania, outraged Americans.",
            "To support the Allied Powers (England, France, Italy, and Russia)": "The U.S. had strong economic and cultural ties to Britain and France.",
            "To oppose the Central Powers (Germany, Austria-Hungary, the Ottoman Empire, and Bulgaria)": "The Zimmerman Telegram, where Germany tried to ally with Mexico against the U.S., was the final straw."
        },
        "102": {
            "1920": "The year the 19th Amendment was ratified, legally guaranteeing women the right to vote.",
            "After World War I": "President Wilson supported suffrage as a 'war measure' to acknowledge women's role in the war effort.",
            "(With the) 19 th Amendment": "It states that the right of citizens to vote shall not be denied or abridged by the United States or by any State on account of sex."
        },
        "103": {
            "Longest economic recession in modern history": "It began with the Stock Market Crash of 1929 and lasted until World War II, causing widespread poverty and unemployment."
        },
        "104": {
            "The Great Crash (1929)": "The stock market lost nearly 90% of its value between 1929 and 1932."
        },
        "105": {
            "(Franklin) Roosevelt": "FDR is the only president to serve more than two terms. He created the 'New Deal' to help Americans during the Depression."
        },
        "106": {
            "(Bombing of) Pearl Harbor": "President Roosevelt called December 7, 1941, 'a date which will live in infamy'.",
            "Japanese attacked Pearl Harbor": "The attack destroyed much of the Pacific fleet but failed to hit the aircraft carriers.",
            "To support the Allied Powers (England, France, and Russia)": "The U.S. was already providing supplies through the Lend-Lease Act before officially entering the war.",
            "To oppose the Axis Powers (Germany, Italy, and Japan)": "The war was a global struggle against fascism and militarism."
        },
        "107": {
            "General during World War II": "“Ike” planned the D-Day invasion of Normandy, the largest amphibious assault in history.",
            "President at the end of (during) the Korean War": "He campaigned on the promise 'I will go to Korea' to end the stalled conflict.",
            "34 th president of the United States": "He warned against the 'military-industrial complex' in his farewell address."
        },
        "108": {
            "Soviet Union": "An ideological rival that promoted communism and totalitarianism against Western democracy.",
            "USSR": "Stood for Union of Soviet Socialist Republics, a massive empire spanning 11 time zones.",
            "Russia": "The primary successor state to the Soviet Union after its collapse in 1991."
        },
        "109": {
            "Communism": "The U.S. policy was 'containment'—stopping the spread of communism to new countries.",
            "Nuclear war": "The 'Cuban Missile Crisis' in 1962 was the closest the world ever came to nuclear destruction."
        },
        "110": {
            "To stop the spread of communism": "The North Korean invasion of the South was seen as the first military test of the Cold War containment policy."
        },
        "111": {
            "To stop the spread of communism": "The U.S. feared the 'Domino Theory'—that if Vietnam fell, all of Southeast Asia would become communist."
        },
        "112": {
            "Fought to end racial discrimination": "Through nonviolent protest, legal challenges, and marches, it ended legalized segregation in the South."
        },
        "113": {
            "Fought for civil rights": "He advocated for civil disobedience, inspired by Mahatma Gandhi.",
            "Worked for equality for all Americans": "His work led to the Civil Rights Act of 1964 and the Voting Rights Act of 1965.",
            "Worked to ensure that people would “not be judged by the color of their skin, but by the content of their character”": "This quote defines the American ideal of merit and equality."
        },
        "114": {
            "To force the Iraqi military from Kuwait": "Operation Desert Storm was a massive coalition effort that liberated Kuwait in roughly 100 hours of ground combat."
        },
        "115": {
            "Terrorists attacked the United States": "19 hijackers from Al-Qaeda carried out suicide attacks using commercial airplanes.",
            "Terrorists took over two planes and crashed them into the World Trade Center in New York City": "The destruction of the Twin Towers killed nearly 3,000 people and traumatized the nation.",
            "Terrorists took over a plane and crashed into the Pentagon in Arlington, Virginia": "184 people were killed at the symbol of American military power.",
            "Terrorists took over a plane originally aimed at Washington, D.C., and crashed in a field in Pennsylvania": "Passengers on United Flight 93 stormed the cockpit, preventing the plane from hitting the Capitol or White House."
        },
        "116": {
            "(Global) War on Terror": "A shift in U.S. policy to preemptively strike terrorist groups and the states that harbor them.",
            "War in Afghanistan": "The longest war in U.S. history, launched to find Osama bin Laden and destroy Al-Qaeda.",
            "War in Iraq": "A controversial conflict aimed at ending the regime of Saddam Hussein."
        },
        "117": {
            "Apache": "Legendary warriors like Geronimo fought to protect their homeland in the Southwest.",
            "Blackfeet": "Controlled a vast territory in Montana and were known for their powerful alliance.",
            "Cayuga": "A member of the Iroquois Confederacy, originally from the Finger Lakes region of New York.",
            "Cherokee": "Developed their own written language (Sequoyah) and constitution before being forced on the Trail of Tears.",
            "Cheyenne": "Known for their Dog Soldiers society and their role in the Battle of Little Bighorn.",
            "Chippewa": "Also known as Ojibwe, they are one of the largest tribal populations, centered around the Great Lakes.",
            "Choctaw": "The first tribe to be forced to relocate to Oklahoma; they aided the Irish during the Potato Famine.",
            "Creek": "Also known as Muscogee, they were a powerful confederacy in the Southeast.",
            "Crow": "Known for their striking traditional dress and their alliance with the U.S. Army against the Sioux.",
            "Hopi": "Farmers who have lived in the same villages in Arizona for nearly a thousand years (e.g., Oraibi).",
            "Huron": "Also known as Wyandot, they were major traders who allied with the French.",
            "Inupiat": "Native people of Alaska's North Slope, experts at surviving in the Arctic.",
            "Lakota": "The stereotypical 'Plains Indian' culture with tipis and buffalo financing; warriors of Sitting Bull and Crazy Horse.",
            "Mohawk": "Fierce warriors of the Iroquois League, now also famous for their skill as high-altitude ironworkers.",
            "Mohegan": "A maritime tribe from Connecticut, now owners of the Mohegan Sun enterprise.",
            "Navajo": "The 'Dine' helped win WWII with their unbreakable Code based on their complex language.",
            "Oneida": "Known as America's 'First Allies' for fighting alongside the colonists in the Revolutionary War.",
            "Onondaga": "The 'Keepers of the Fire' for the Iroquois Confederacy, hosting the Grand Council.",
            "Pueblo": "Revolted against the Spanish in 1680 (Pueblo Revolt) to preserve their religion and culture.",
            "Seminole": "The 'Unconquered People' who retreated into the Everglades and never surrendered to the U.S. government.",
            "Seneca": "The largest nation of the Iroquois Confederacy, traditionally guarding the western frontier.",
            "Shawnee": "Their leader Tecumseh attempted to form a massive pan-Indian alliance to stop U.S. expansion.",
            "Sioux": "A confederation of several tribes (Lakota, Dakota, Nakota) on the Great Plains.",
            "Teton": "The westernmost division of the Sioux, comprising seven tribal bands.",
            "Tuscarora For a complete list of tribes, please visit bia.gov.": "Originally from the Carolinas, they migrated north to become the sixth nation of the Iroquois.",
            "Tuscarora": "Migrated north to join the Iroquois Confederacy as the sixth nation."
        },
        "118": {
            "Light bulb": "Edison tested thousands of materials before finding the right carbon filament.",
            "Automobile (cars, internal combustion engine)": "The Model T revolutionized American life by giving freedom of movement to the average family.",
            "Skyscrapers": "Chicago and New York raced to build higher, symbolizing American optimism and economic power.",
            "Airplane": "From a 12-second flight at Kitty Hawk to landing on the Moon in less than 70 years.",
            "Assembly line": "Drastically reduced the time to build a car from 12 hours to 90 minutes.",
            "Landing on the moon": "'One small step for man, one giant leap for mankind.'",
            "Integrated circuit (IC) SYMBOLS AND HOLIDAYS": "The microchip is the brain of every computer and phone we use today, invented by Americans Jack Kilby and Robert Noyce."
        },
        "119": {
            "Washington, D.C.": "Pierre L'Enfant designed the city with wide avenues and grand circles to resemble European capitals."
        },
        "120": {
            "New York (Harbor)": "A gift from France, it was the first thing millions of immigrants saw as they arrived in America.",
            "Liberty Island [Also acceptable are New Jersey, near New York City, and on the Hudson (River).]": "Originally called Bedloe's Island, it was renamed in 1956."
        },
        "121": {
            "(Because there were) 13 original colonies": "The red and white stripes honor the original foundation of the country.",
            "(Because the stripes) represent the original colonies": "We keep the 13 stripes even as we add stars, to remember where we started."
        },
        "122": {
            "(Because there is) one star for each state": "If a new state joins, a new star is added on the following July 4th.",
            "(Because) each star represents a state": "The stars are collectively a symbol of the Union.",
            "(Because there are) 50 states": "Hawaii was the last state added in 1959, bringing the total to 50."
        },
        "123": {
            "The Star-Spangled Banner": "It didn't become the official national anthem until 1931!"
        },
        "124": {
            "Out of many, one": "It refers to the 13 colonies uniting into one nation, and now refers to our diverse people forming one society.",
            "We all become one": "America is often called a 'melting pot' where distinct cultures blend into a unified whole."
        },
        "125": {
            "A holiday to celebrate U.S. independence (from Britain)": "Marked by parades, fireworks, and barbecues.",
            "The country’s birthday": "Technically the date the Declaration was adopted, not signed (which was mostly in August)."
        },
        "126": {
            "New Year’s Day": "A day of celebration and resolutions.",
            "Martin Luther King, Jr. Day": "A day of service reflecting on racial equality.",
            "Presidents Day (Washington’s Birthday)": "Originally just Washington's Birthday, now honors Lincoln too.",
            "Memorial Day": "The unofficial start of summer, but its true purpose is mourning the fallen.",
            "Juneteenth": "The newest federal holiday, celebrating the news of freedom reaching the last slaves in Texas in 1865.",
            "Independence Day": "The quintessential American holiday celebrating freedom.",
            "Labor Day": "Honors the contributions of workers and the labor movement; unofficial end of summer.",
            "Columbus Day": "A controversial holiday; many states now celebrate Indigenous Peoples' Day instead.",
            "Veterans Day": "Originally Armistice Day (end of WWI), now honors all living veterans.",
            "Thanksgiving Day": "A day for family, food, and gratitude.",
            "Christmas Day": "A widely celebrated religious and secular holiday."
        },
        "127": {
            "A holiday to honor soldiers who died in military service": "Remember: Memorial Day is for the dead; Veterans Day is for the living."
        },
        "128": {
            "A holiday to honor people in the (U.S.) military": "We thank veterans for their service and sacrifice in protecting our freedoms.",
            "A holiday to honor people who have served (in the U.S. military)": "There are over 18 million brave veterans living in the United States today."
        }
    }

    # Merge
    for q_id, answers in new_data.items():
        if q_id not in data:
            data[q_id] = {}
        for ans_text, elaboration in answers.items():
            data[q_id][ans_text] = elaboration

    with open(FILE_PATH, 'w') as f:
        json.dump(data, f, indent=2)
    
    print("Gemini data updated successfully.")

if __name__ == "__main__":
    update_data()
