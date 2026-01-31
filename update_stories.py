import json

# Load existing stories
with open('stories_data.json', 'r') as f:
    data = json.load(f)

# Updates
updates = {
    # 48. Cabinet Positions
    "48": {
        "Secretary of Agriculture": "Oversees the American farming industry, food safety, and nutrition programs like school lunches.",
        "Secretary of Commerce": "Promotes job creation and economic growth by supporting U.S. businesses and trade.",
        "Secretary of Defense": "The CEO of the military. They manage the Army, Navy, Air Force, and Marines to protect national security.",
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
        "Vice President": "Ready to take over the Presidency if needed, and also casts tie-breaking votes in the Senate."
    },
    
    # 51. Rights of Everyone
    "51": {
        "Freedom of expression": "You can express your ideas and opinions through art, music, or clothing without government censorship.",
        "Freedom of speech": "You can criticize the government or share unpopular opinions without fear of going to jail.",
        "Freedom of assembly": "You can gather peacefully in groups to protest or support a cause.",
        "Freedom to petition the government": "You can ask the government to fix a problem or change a law.",
        "Freedom of religion": "You can practice any religion you want, or no religion at all.",
        "The right to bear arms": "You have the right to own weapons for self-defense, as protected by the Second Amendment."
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

    # 92. Problems leading to Civil War
    "92": {
        "Slavery": "The South wanted to keep slavery for their plantation economy, while the North largely opposed its expansion.",
        "Economic reasons": "The industrial North and agricultural South had very different economic needs and disagreed on tariffs.",
        "States’ rights": "Southern states argued they had the right to ignore federal laws they didn't like, including potential bans on slavery."
    },

    # 94. Lincoln
    "94": {
        "Freed the slaves (Emancipation Proclamation)": "He issued the order that declared all slaves in Confederate territory to be forever free.",
        "Saved (or preserved) the Union": "He refused to let the Southern states break away, fighting a bloody war to keep the United States as one country.",
        "Led the United States during the Civil War": "He guided the nation through its darkest and deadliest four years."
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

    # 117. Tribes (Examples, generic vs specific is hard but let's try a few obvious ones)
    "117": {
        "Cherokee": "One of the largest tribes. They were tragically forced from their lands in the southeast on the 'Trail of Tears'.",
        "Navajo": "The largest federally recognized tribe. Their 'Code Talkers' used their language to create an unbreakable code during WWII.",
        "Sioux": "Known for resistance leaders like Sitting Bull and Crazy Horse, and the Battle of Little Bighorn.",
        "Apache": "A southwestern tribe known for fierce resistance leaders like Geronimo.",
        "Iroquois": "Their Confederacy (Haudenosaunee) is one of the world's oldest participatory democracies and influenced the U.S. Constitution.",
        "DEFAULT": "One of the many sovereign tribal nations that inhabited North America long before European colonization."
    },
    
    # 126. Holidays
    "126": {
        "New Year’s Day": "Celebrated on January 1st to mark the beginning of the new Gregorian calendar year.",
        "Martin Luther King, Jr. Day": "Celebrated in January to honor the civil rights leader's birthday and his fight for equality.",
        "Presidents’ Day": "Celebrated in February, originally to honor George Washington, now honoring all presidents.",
        "Memorial Day": "A solemn day in May to mourn the military personnel who have died while serving in the armed forces.",
        "Juneteenth": "Celebrated on June 19th to commemorate the end of slavery in the U.S. (when news finally reached Texas in 1865).",
        "Independence Day": "July 4th! The anniversary of the publication of the Declaration of Independence in 1776.",
        "Labor Day": "Celebrated in September to honor the American labor movement and the contributions of workers.",
        "Columbus Day": "Commemorates the landing of Christopher Columbus in the Americas in 1492.",
        "Veterans Day": "Celebrated in November to honor all military veterans who have served in the U.S. Armed Forces.",
        "Thanksgiving": "A harvest festival celebrated in November, modeled on a 1621 harvest feast sharing between Colonists and the Wampanoag.",
        "Christmas": "Celebrated on December 25th, originally a Christian holiday, now also a federal holiday."
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
