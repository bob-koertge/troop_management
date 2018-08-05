from django.core.management.base import BaseCommand
from troop.models import Rank, Position, MeritBadge, User, RankRequirement


class Command(BaseCommand):

    def _create_base_data(self):
        User(password='pbkdf2_sha256$120000$i4U0o9UJ0Dz9$Yo/0fbRT16kVA+/bXsodHrZI/QZJW3DxcSIMFvVzoYI=',
             is_superuser=True,
             username='admin',
             email='admin@example.com',
             is_staff=True,
             is_active=True,
             ).save()
        print('Loading Rank')
        just_joined = Rank(name='Just Joined')
        scout = Rank(name='Scout')
        tenderfoot = Rank(name='Tenderfoot')
        second_class = Rank(name='Second Class')
        first_class = Rank(name='First Class')
        star = Rank(name='Star')
        life = Rank(name='Life')
        eagle = Rank(name='Eagle')

        just_joined.save()
        scout.save()
        tenderfoot.save()
        second_class.save()
        first_class.save()
        star.save()
        life.save()
        eagle.save()
        print('Loading Position')
        Position(name='Scoutmaster', short_name="SM",
                 is_youth_position=False).save()
        Position(name='Commitee Chair', short_name="CC",
                 is_youth_position=False).save()
        Position(name='Commitee Member', short_name="MC",
                 is_youth_position=False).save()
        Position(name='Charter Organization Representative',
                 short_name="CR", is_youth_position=False).save()
        Position(name='Institutional Head', short_name="IH",
                 is_youth_position=False).save()
        Position(name='ScoutParent Unit Coordinator',
                 short_name="PC", is_youth_position=False).save()
        Position(name='ScoutParent', short_name="PS",
                 is_youth_position=False).save()
        Position(name='Assistant Scoutmaster', short_name="AS",
                 is_youth_position=False).save()
        Position(name='Scouter Reserve', short_name="91",
                 is_youth_position=False).save()
        Position(name='College Scouter Reserve',
                 short_name="92", is_youth_position=False).save()
        Position(name='Senior Patrol Leader', short_name='SPL').save()
        Position(name='Assistant Senior Patrol Leader',
                 short_name='ASPL').save()
        Position(name='Patrol Leader', short_name='PL').save()
        Position(name='Troop Guide', short_name='TG').save()
        Position(name='Quartermaster', short_name='QM').save()
        Position(name='Scribe', short_name='SC').save()
        Position(name='Den Chief', short_name='DC').save()
        Position(name='Chaplain Aide', short_name='CA').save()
        Position(name='Historian', short_name='HI').save()
        Position(name='Instructor', short_name='IN').save()
        Position(name='Webmaster', short_name='WE').save()
        Position(name='Order of Arrow Representative', short_name='OA').save()
        Position(name='Outdoor Ethics Guide', short_name='OE').save()
        Position(name='Junior Assistant Scoutmaster',
                 short_name='JASM').save()
        print('Loading MeritBadge')
        MeritBadge(name="American Business", is_eagle_required=False).save()
        MeritBadge(name="American Cultures", is_eagle_required=False).save()
        MeritBadge(name="American Heritage", is_eagle_required=False).save()
        MeritBadge(name="American Labor", is_eagle_required=False).save()
        MeritBadge(name="Animal Science", is_eagle_required=False).save()
        MeritBadge(name="Animation", is_eagle_required=False).save()
        MeritBadge(name="Archaeology", is_eagle_required=False).save()
        MeritBadge(name="Archery", is_eagle_required=False).save()
        MeritBadge(name="Architecture", is_eagle_required=False).save()
        MeritBadge(name="Art", is_eagle_required=False).save()
        MeritBadge(name="Astronomy", is_eagle_required=False).save()
        MeritBadge(name="Athletics", is_eagle_required=False).save()
        MeritBadge(name="Automotive Maintenance",
                   is_eagle_required=False).save()
        MeritBadge(name="Aviation", is_eagle_required=False).save()
        MeritBadge(name="Backpacking", is_eagle_required=False).save()
        MeritBadge(name="Basketry", is_eagle_required=False).save()
        MeritBadge(name="Bird Study", is_eagle_required=False).save()
        MeritBadge(name="Bugling", is_eagle_required=False).save()
        MeritBadge(name="Camping", is_eagle_required=True).save()
        MeritBadge(name="Canoeing", is_eagle_required=False).save()
        MeritBadge(name="Chemistry", is_eagle_required=False).save()
        MeritBadge(name="Chess", is_eagle_required=False).save()
        MeritBadge(name="Citizenship in the Community",
                   short_name='Cit In Community', is_eagle_required=True).save()
        MeritBadge(name="Citizenship in the Nation",
                   short_name='Cit In Nation', is_eagle_required=True).save()
        MeritBadge(name="Citizenship in the World",
                   short_name='Cit In World', is_eagle_required=True).save()
        MeritBadge(name="Climbing", is_eagle_required=False).save()
        MeritBadge(name="Coin Collecting", is_eagle_required=False).save()
        MeritBadge(name="Collections", is_eagle_required=False).save()
        MeritBadge(name="Communications", short_name='Communication',
                   is_eagle_required=True).save()
        MeritBadge(name="Composite Materials", is_eagle_required=False).save()
        MeritBadge(name="Cooking", is_eagle_required=True).save()
        MeritBadge(name="Crime Prevention", is_eagle_required=False).save()
        MeritBadge(name="Cycling", is_eagle_required=True).save()
        MeritBadge(name="Dentistry", is_eagle_required=False).save()
        MeritBadge(name="Digital Technology", is_eagle_required=False).save()
        MeritBadge(name="Disabilities Awareness",
                   is_eagle_required=False).save()
        MeritBadge(name="Dog Care", is_eagle_required=False).save()
        MeritBadge(name="Drafting", is_eagle_required=False).save()
        MeritBadge(name="Electricity", is_eagle_required=False).save()
        MeritBadge(name="Electronics", is_eagle_required=False).save()
        MeritBadge(name="Emergency Preparedness",
                   short_name='Emergency Prep', is_eagle_required=True).save()
        MeritBadge(name="Energy", is_eagle_required=False).save()
        MeritBadge(name="Engineering", is_eagle_required=False).save()
        MeritBadge(name="Entrepreneurship", is_eagle_required=False).save()
        MeritBadge(name="Environmental Science",
                   short_name='Environmental Sci', is_eagle_required=True).save()
        MeritBadge(name="Family Life", is_eagle_required=True).save()
        MeritBadge(name="Farm Mechanics", is_eagle_required=False).save()
        MeritBadge(name="Fingerprinting", is_eagle_required=False).save()
        MeritBadge(name="Fire Safety", is_eagle_required=False).save()
        MeritBadge(name="First Aid", is_eagle_required=True).save()
        MeritBadge(name="Fish and Wildlife Management",
                   short_name='Fish and Wildlife', is_eagle_required=False).save()
        MeritBadge(name="Fishing", is_eagle_required=False).save()
        MeritBadge(name="Fly Fishing", is_eagle_required=False).save()
        MeritBadge(name="Forestry", is_eagle_required=False).save()
        MeritBadge(name="Game Design", is_eagle_required=False).save()
        MeritBadge(name="Gardening", is_eagle_required=False).save()
        MeritBadge(name="Genealogy", is_eagle_required=False).save()
        MeritBadge(name="Geocaching", is_eagle_required=False).save()
        MeritBadge(name="Geology", is_eagle_required=False).save()
        MeritBadge(name="Golf", is_eagle_required=False).save()
        MeritBadge(name="Graphic Arts", is_eagle_required=False).save()
        MeritBadge(name="Hiking", is_eagle_required=True).save()
        MeritBadge(name="Home Repairs", is_eagle_required=False).save()
        MeritBadge(name="Horsemanship", is_eagle_required=False).save()
        MeritBadge(name="Indian Lore", is_eagle_required=False).save()
        MeritBadge(name="Insect Study", is_eagle_required=False).save()
        MeritBadge(name="Inventing", is_eagle_required=False).save()
        MeritBadge(name="Journalism", is_eagle_required=False).save()
        MeritBadge(name="Kayaking", is_eagle_required=False).save()
        MeritBadge(name="Landscape Architecture",
                   is_eagle_required=False).save()
        MeritBadge(name="Law", is_eagle_required=False).save()
        MeritBadge(name="Leatherwork", is_eagle_required=False).save()
        MeritBadge(name="Lifesaving", is_eagle_required=True).save()
        MeritBadge(name="Mammal Study", is_eagle_required=False).save()
        MeritBadge(name="Medicine", is_eagle_required=False).save()
        MeritBadge(name="Metalwork", is_eagle_required=False).save()
        MeritBadge(name="Mining in Society", is_eagle_required=False).save()
        MeritBadge(name="Model Design and Building",
                   is_eagle_required=False).save()
        MeritBadge(name="Motorboating", is_eagle_required=False).save()
        MeritBadge(name="Moviemaking", is_eagle_required=False).save()
        MeritBadge(name="Music", is_eagle_required=False).save()
        MeritBadge(name="Nature", is_eagle_required=False).save()
        MeritBadge(name="Nuclear Science", is_eagle_required=False).save()
        MeritBadge(name="Oceanography", is_eagle_required=False).save()
        MeritBadge(name="Orienteering", is_eagle_required=False).save()
        MeritBadge(name="Painting", is_eagle_required=False).save()
        MeritBadge(name="Personal Fitness", is_eagle_required=True).save()
        MeritBadge(name="Personal Management", is_eagle_required=True).save()
        MeritBadge(name="Pets", is_eagle_required=False).save()
        MeritBadge(name="Photography", is_eagle_required=False).save()
        MeritBadge(name="Pioneering", is_eagle_required=False).save()
        MeritBadge(name="Plant Science", is_eagle_required=False).save()
        MeritBadge(name="Plumbing", is_eagle_required=False).save()
        MeritBadge(name="Pottery", is_eagle_required=False).save()
        MeritBadge(name="Programming", is_eagle_required=False).save()
        MeritBadge(name="Public Health", is_eagle_required=False).save()
        MeritBadge(name="Public Speaking", is_eagle_required=False).save()
        MeritBadge(name="Pulp and Paper", is_eagle_required=False).save()
        MeritBadge(name="Radio", is_eagle_required=False).save()
        MeritBadge(name="Railroading", is_eagle_required=False).save()
        MeritBadge(name="Reading", is_eagle_required=False).save()
        MeritBadge(name="Reptile and Amphibian Study",
                   short_name='Reptile/Amphibian', is_eagle_required=False).save()
        MeritBadge(name="Rifle Shooting", is_eagle_required=False).save()
        MeritBadge(name="Robotics", is_eagle_required=False).save()
        MeritBadge(name="Rowing", is_eagle_required=False).save()
        MeritBadge(name="Safety", is_eagle_required=False).save()
        MeritBadge(name="Salesmanship", is_eagle_required=False).save()
        MeritBadge(name="Scholarship", is_eagle_required=False).save()
        MeritBadge(name="Scouting Heritage", is_eagle_required=False).save()
        MeritBadge(name="Scuba Diving", is_eagle_required=False).save()
        MeritBadge(name="Sculpture", is_eagle_required=False).save()
        MeritBadge(name="Search and Rescue", is_eagle_required=False).save()
        MeritBadge(name="Shotgun Shooting", is_eagle_required=False).save()
        MeritBadge(name="Signs, Signals, and Codes",
                   is_eagle_required=False).save()
        MeritBadge(name="Skating", is_eagle_required=False).save()
        MeritBadge(name="Small Boat Sailing", is_eagle_required=False).save()
        MeritBadge(name="Snow Sports", is_eagle_required=False).save()
        MeritBadge(name="Soil and Water Conservation",
                   short_name='Soil and Water', is_eagle_required=False).save()
        MeritBadge(name="Space Exploration", is_eagle_required=False).save()
        MeritBadge(name="Sports", is_eagle_required=False).save()
        MeritBadge(name="Stamp Collecting", is_eagle_required=False).save()
        MeritBadge(name="Surveying", is_eagle_required=False).save()
        MeritBadge(name="Sustainability", is_eagle_required=True).save()
        MeritBadge(name="Swimming", is_eagle_required=True).save()
        MeritBadge(name="Textile", is_eagle_required=False).save()
        MeritBadge(name="Theater", is_eagle_required=False).save()
        MeritBadge(name="Traffic Safety", is_eagle_required=False).save()
        MeritBadge(name="Truck Transportation", is_eagle_required=False).save()
        MeritBadge(name="Veterinary Medicine", is_eagle_required=False).save()
        MeritBadge(name="Water Sports", is_eagle_required=False).save()
        MeritBadge(name="Weather", is_eagle_required=False).save()
        MeritBadge(name="Welding", is_eagle_required=False).save()
        MeritBadge(name="Whitewater", is_eagle_required=False).save()
        MeritBadge(name="Wilderness Survival", is_eagle_required=False).save()
        MeritBadge(name="Wood Carving", is_eagle_required=False).save()
        MeritBadge(name="Woodwork", is_eagle_required=False).save()
        print('Loading RankRequirement for Scout')
        RankRequirement(sort_order=1, number='', is_header=True,
                        header='Scouts:', rank=scout, revision='2016').save()
        RankRequirement(sort_order=2, number='1a', revision='2016',
                        short_desc='Repeat/Explain Oath/Law/Motto/Slogan',
                        description=' Repeat from memory the Scout Oath, Scout Law, Scout motto, and Scout slogan. In your own words, explain their meaning.',
                        rank=scout).save()
        RankRequirement(sort_order=3, number='1b', revision='2016',
                        short_desc='Explain Scout Spirit',
                        description='Explain what Scout spirit is. Describe some ways you have shown Scout spirit by practicing the Scout Oath, Scout Law, Scout motto, and Scout slogan.',
                        rank=scout).save()
        RankRequirement(sort_order=4, number='1c', revision='2016',
                        short_desc='Demo/Explain Scout Sign/salute/handshake',
                        description='Demonstrate the Boy Scout sign, salute, and handshake. Explain when they should be used.',
                        rank=scout).save()
        RankRequirement(sort_order=5, number='1d', revision='2016',
                        short_desc='Describe 1st Class Badge',
                        description='Demonstrate the Boy Scout sign, salute, and handshake. Explain when they should be usedDescribe the First Class Scout badge and tell what each part stands for. Explain the significance of the First Class Scout badge.',
                        rank=scout).save()
        RankRequirement(sort_order=6, number='1e', revision='2016',
                        short_desc='Repeat/Explain Outdoor Code',
                        description='Repeat from memory the Outdoor Code. In your own words, explain what the Outdoor Code means to you.',
                        rank=scout).save()
        RankRequirement(sort_order=7, number='1f', revision='2016',
                        short_desc='Repeat/Explain Pledge',
                        description='Repeat from memory the Pledge of Allegiance. In your own words, explain its meaning.',
                        rank=scout).save()
        RankRequirement(sort_order=7, number='', is_header=True,
                        header='After attending at least one Boy Scout troop meeting, do the following:', rank=scout, revision='2016').save()
        RankRequirement(sort_order=8, number='2a', revision='2016', rank=scout, short_desc='Describe Scout Leadership',
                        description='Describe how the Scouts in the troop provide its leadership.').save()
        RankRequirement(sort_order=9, number='2b', revision='2016', rank=scout, short_desc='Describe 4 Steps of Advancement',
                        description='Describe the four steps of Boy Scout advancement.').save()
        RankRequirement(sort_order=10, number='2c', revision='2016', rank=scout, short_desc='Describe Ranks',
                        description='Describe what the Boy Scout ranks are and how they are earned.').save()
        RankRequirement(sort_order=11, number='2d', revision='2016', rank=scout, short_desc='Describe Merit Badges',
                        description='Describe what merit badges are and how they are earned.').save()
        RankRequirement(sort_order=12, number='', is_header=True,
                        header='Patrol:', rank=scout, revision='2016').save()
        RankRequirement(sort_order=13, number='3a', revision='2016', rank=scout, short_desc='Explain Patrol Method',
                        description='Explain the patrol method. Describe the types of patrols that are used in your troop.').save()
        RankRequirement(sort_order=14, number='3b', revision='2016', rank=scout, short_desc='Patrol Name/Flag/Yell',
                        description='Become familiar with your patrol name, emblem, flag, and yell. Explain how these items create patrol spirit.').save()
        RankRequirement(sort_order=15, number='', is_header=True,
                        header='Knots and Rope:', rank=scout, revision='2016').save()
        RankRequirement(sort_order=16, number='4a', revision='2016', rank=scout, short_desc='Knots/Hitches',
                        description='Show how to tie a square knot, two half-hitches, and a taut-line hitch. Explain how each knot is used.').save()
        RankRequirement(sort_order=17, number='4b', revision='2016', rank=scout, short_desc='Rope Care & Fusing',
                        description='Show the proper care of a rope by learning how to whip and fuse the ends of different kinds of rope.').save()

        RankRequirement(sort_order=16, number='5', revision='2016', rank=scout, short_desc='Pocketknife Safety',
                        description='Demonstrate your knowledge of pocketknife safety.').save()

        RankRequirement(sort_order=17, number='6', revision='2016', rank=scout, short_desc='Child Abuse & Cyberchip',
                        description='With your parent or guardian, complete the exercises in the pamphlet "How to Protect Your Children from Child Abuse: A Parents Guide" and earn the Cyber Chip Award for your grade.').save()

        RankRequirement(sort_order=18, number='7', revision='2016', rank=scout, short_desc='Scoutmaster Conference',
                        description='Since joining the troop and while working on the Scout rank, participate in a Scoutmaster conference.').save()

        print('Loading RankRequirement for Tenderfoot')
        RankRequirement(sort_order=1, number='', is_header=True,
                        header='Camping and Outdoor Ethics:', rank=tenderfoot, revision='2016').save()
        RankRequirement(sort_order=2, number='1a', revision='2016', rank=tenderfoot,
                        short_desc='Present Overnight Gear',
                        description='Present yourself to your leader, prepared for an overnight camping trip. Show the personal and camping gear you will use. Show the right way to pack and carry it.').save()
        RankRequirement(sort_order=3, number='1b', revision='2016', rank=tenderfoot,
                        short_desc='Overnight in Tent',
                        description='Spend at least one night on a patrol or troop campout. Sleep in a tent you have helped pitch.').save()
        RankRequirement(sort_order=4, number='1c', revision='2016', rank=tenderfoot,
                        short_desc='Outdoor Code',
                        description='Tell how you practiced the Outdoor Code on a campout or outing').save()
        RankRequirement(sort_order=5, number='', is_header=True,
                        header='Cooking:', rank=tenderfoot, revision='2016').save()
        RankRequirement(sort_order=6, number='2a', revision='2016', rank=tenderfoot,
                        short_desc='Assist Meal Prep',
                        description='On the campout, assist in preparing one of the meals. Tell why it is important for each patrol member to share in meal preparation and cleanup.').save()
        RankRequirement(sort_order=7, number='2b', revision='2016', rank=tenderfoot,
                        short_desc='Cleaning Safety',
                        description='While on a campout, demonstrate an appropriate method of safely cleaning items used to prepare, serve, and eat a meal.').save()
        RankRequirement(sort_order=8, number='2c', revision='2016', rank=tenderfoot,
                        short_desc='Eating as Patrol',
                        description='Explain the importance of eating together as a patrol').save()
        RankRequirement(sort_order=9, number='', is_header=True,
                        header='Tools:', rank=tenderfoot, revision='2016').save()
        RankRequirement(sort_order=10, number='3a', revision='2016', rank=tenderfoot,
                        short_desc='Square Knot',
                        description='Demonstrate a practical use of the square knot.').save()
        RankRequirement(sort_order=11, number='3b', revision='2016', rank=tenderfoot,
                        short_desc='Two Half-Hitches',
                        description='Demonstrate a practical use of two half-hitches.').save()
        RankRequirement(sort_order=12, number='3c', revision='2016', rank=tenderfoot,
                        short_desc='Taut-Line Hitch',
                        description='Demonstrate a practical use of the taut-line hitch.').save()
        RankRequirement(sort_order=13, number='3d', revision='2016', rank=tenderfoot,
                        short_desc='Use/care outdoor tools',
                        description='Demonstrate proper care, sharpening, and use of the knife, saw, and ax. Describe when each should be used.').save()
        RankRequirement(sort_order=14, number='', is_header=True,
                        header='First Aid and Nature:', rank=tenderfoot, revision='2016').save()
        RankRequirement(sort_order=15, number='4a', revision='2016', rank=tenderfoot,
                        short_desc='First Aid',
                        description="""Show first aid for the following:
                        •	Simple cuts and scrapes
                        •	Blisters on the hand and foot
                        •	Minor(thermal / heat) burns or scalds(superficial, or first degree)
                        •	Bites or stings of insects or ticks
                        •	Venomous snakebite
                        •	Nosebleed
                        •	Frostbite and sunburn
                        •	Choking""").save()
        RankRequirement(sort_order=16, number='4b', revision='2016', rank=tenderfoot,
                        short_desc='Hazardous Plants',
                        description='Describe common poisonous or hazardous plants; identify any that grow in your local area or campsite location. Tell how to treat for exposure to them.').save()
        RankRequirement(sort_order=17, number='4c', revision='2016', rank=tenderfoot,
                        short_desc='Injury Prevention',
                        description='Tell what you can do while on a campout or other outdoor activity to prevent or reduce the occurrence of injuries or exposure listed in Tenderfoot requirements 4a and 4b.').save()
        RankRequirement(sort_order=18, number='4d', revision='2016', rank=tenderfoot,
                        short_desc='First Aid Kit',
                        description='Assemble a personal first-aid kit to carry with you on future campouts and hikes. Tell how each item in the kit would be used.').save()
        RankRequirement(sort_order=19, number='', is_header=True,
                        header='Hiking:', rank=tenderfoot, revision='2016').save()
        RankRequirement(sort_order=20, number='5a', revision='2016', rank=tenderfoot,
                        short_desc='Buddy System',
                        description='Explain the importance of the buddy system as it relates to your personal safety on outings and in your neighborhood. Use the buddy system while on a troop or patrol outing.').save()
        RankRequirement(sort_order=21, number='5b', revision='2016', rank=tenderfoot,
                        short_desc='Lost on Campout/Hike',
                        description='Describe what to do if you become lost on a hike or campout.').save()
        RankRequirement(sort_order=22, number='5c', revision='2016', rank=tenderfoot,
                        short_desc='Safe Hiking',
                        description='Explain the rules of safe hiking, both on the highway and cross-country, during the day and at night.').save()
        RankRequirement(sort_order=23, number='', is_header=True,
                        header='Fitness:', rank=tenderfoot, revision='2016').save()
        RankRequirement(sort_order=24, number='6a', revision='2016', rank=tenderfoot,
                        short_desc='Record Fitness',
                        description="""Record your best in the following tests:
                            Push-ups ________ (Record the number done correctly in 60 seconds.)
                            Sit-ups or curl-ups ________ (Record the number done correctly in 60 seconds.)
                            Back-saver sit-and-reach (Record the distance stretched.)
                            1-mile walk/run _____________ (Record the time.)""").save()
        RankRequirement(sort_order=25, number='6b', revision='2016', rank=tenderfoot,
                        short_desc='30 day Fitness Plan',
                        description='Develop and describe a plan for improvement in each of the activities listed in Tenderfoot requirement 6a. Keep track of your activity for at least 30 days.').save()
        RankRequirement(sort_order=26, number='6c', revision='2016', rank=tenderfoot,
                        short_desc='Fitness Improvement',
                        description=""" Show improvement (of any degree) in each activity listed in Tenderfoot requirement 6a after practicing for 30 days.
                        Push-ups ________ (Record the number done correctly in 60 seconds.)
                        Sit-ups or curl-ups ________ (Record the number done correctly in 60 seconds.)
                        Back-saver sit-and-reach (Record the distance stretched.)
                        1-mile walk/run _____________ (Record the time.)""").save()
        RankRequirement(sort_order=27, number='', is_header=True,
                        header='Citizenship:', rank=tenderfoot, revision='2016').save()
        RankRequirement(sort_order=28, number='7a', revision='2016', rank=tenderfoot,
                        short_desc='Flag Display/Rise/Lower',
                        description='Demonstrate how to display, raise, lower, and fold the U.S. flag.').save()
        RankRequirement(sort_order=29, number='7b', revision='2016', rank=tenderfoot,
                        short_desc='1hr Service',
                        description='Participate in a total of one hour of service in one or more service projects approved by your Scoutmaster. Explain how your service to others relates to the Scout slogan and Scout motto.').save()
        RankRequirement(sort_order=30, number='', is_header=True,
                        header='Leadership:', rank=tenderfoot, revision='2016').save()
        RankRequirement(sort_order=31, number='8', revision='2016', rank=tenderfoot,
                        short_desc='EDGE method',
                        description='Describe the steps in Scouting’s Teaching EDGE method. Use the Teaching EDGE method to teach another person how to tie the square knot.').save()
        RankRequirement(sort_order=32, number='', is_header=True,
                        header='Scout Spirit:', rank=tenderfoot, revision='2016').save()
        RankRequirement(sort_order=33, number='9', revision='2016', rank=tenderfoot,
                        short_desc='Scout Spirit',
                        description='Demonstrate Scout spirit by living the Scout Oath and Scout Law. Tell how you have done your duty to God and how you have lived four different points of the Scout Law in your everyday life').save()
        RankRequirement(sort_order=34, number='10', revision='2016', rank=tenderfoot,
                        short_desc='SM Conference',
                        description='While working toward the Tenderfoot rank, and after completing Scout rank requirement 7, participate in a Scoutmaster conference..').save()
        RankRequirement(sort_order=35, number='11', revision='2016', rank=tenderfoot,
                        short_desc='Board of Review',
                        description='Successfully complete your board of review for the Tenderfoot rank.').save()

        print('Loading RankRequirement for Second Class')
        RankRequirement(sort_order=36, number='', is_header=True,
                        header='Camping and Outdoor Ethics:', rank=second_class, revision='2016').save()
        RankRequirement(sort_order=37, number='1a', revision='2016', rank=second_class,
                        short_desc='5 Events (3 Nights Camping)',
                        description='Since joining Boy Scouts, participate in five separate troop/patrol activities, at least three of which must be held outdoors. Of the outdoor activities, at least two must include overnight camping. These activities do not include troop or patrol meetings. On campouts, spend the night in a tent that you pitch or other structure that you help erect, such as a lean-to, snow cave, or tepee.').save()
        RankRequirement(sort_order=38, number='1b', revision='2016', rank=second_class,
                        short_desc='Leave No Trace',
                        description='Explain the seven principles of Leave No Trace and tell how you practiced them on a campout or outing. This outing must be different from the one used for "Tenderfoot requirement 1c".').save()
        RankRequirement(sort_order=39, number='1c', revision='2016', rank=second_class,
                        short_desc='Select Patrol Site',
                        description='On one of these campouts, select a location for your patrol site and recommend it to your patrol leader, senior patrol leader, or troop guide. Explain what factors you should consider when choosing a patrol site and where to pitch a tent.').save()
        RankRequirement(sort_order=40, number='', is_header=True,
                        header='Cooking and Tools:', rank=second_class, revision='2016').save()
        RankRequirement(sort_order=41, number='2a', revision='2016', rank=second_class,
                        short_desc='Appropiate Fire Usage',
                        description='Explain when it is appropriate to use a fire for cooking or other purposes and when it would not be appropriate to do so.').save()
        RankRequirement(sort_order=42, number='2b', revision='2016', rank=second_class,
                        short_desc='Tinder/Kindling/Firewood',
                        description='Use the tools listed in Tenderfoot requirement 3d to prepare tinder, kindling, and fuel wood for a cooking fire.').save()
        RankRequirement(sort_order=43, number='2c', revision='2016', rank=second_class,
                        short_desc='Build/Extinguish Fire',
                        description='At an approved outdoor location and time, use the tinder, kindling, and fuel wood from "Second Class requirement 2b" to demonstrate how to build a fire. Unless prohibited by local fire restrictions, light the fire. After allowing the flames to burn safely for at least two minutes, safely extinguish the flames with minimal impact to the fire site.').save()
        RankRequirement(sort_order=44, number='2d', revision='2016', rank=second_class,
                        short_desc='Lightweight Stove',
                        description='Explain when it is appropriate to use a lightweight stove and when it is appropriate to use a propane stove. Set up a lightweight stove or propane stove. Light the stove, unless prohibited by local fire restrictions. Describe the safety procedures for using these types of stoves.').save()
        RankRequirement(sort_order=45, number='2e', revision='2016', rank=second_class,
                        short_desc='Plan/Cook Breakfast or Lunch',
                        description=' On one campout, plan and cook one hot breakfast or lunch, selecting foods from MyPlate or the current USDA nutritional model. Explain the importance of good nutrition. Demonstrate how to transport, store, and prepare the foods you selected.').save()
        RankRequirement(sort_order=46, number='2f', revision='2016', rank=second_class,
                        short_desc='Sheet Bend Knot',
                        description='Demonstrate tying the sheet bend knot. Describe a situation in which you would use this knot.').save()
        RankRequirement(sort_order=47, number='2g', revision='2016', rank=second_class,
                        short_desc='Bowline Knot',
                        description='Demonstrate tying the bowline knot. Describe a situation in which you would use this knot.').save()
        RankRequirement(sort_order=48, number='', is_header=True,
                        header='Navigation:', rank=second_class, revision='2016').save()
        RankRequirement(sort_order=49, number='3a', revision='2016', rank=second_class,
                        short_desc='Orient Map w/ Compass',
                        description='Demonstrate how a compass works and how to orient a map. Use a map to point out and tell the meaning of five map symbols.').save()
        RankRequirement(sort_order=50, number='3b', revision='2016', rank=second_class,
                        short_desc='Map/Compass 5 Mile Hike',
                        description='Using a compass and map together, take a 5-mile hike (or 10 miles by bike) approved by your adult leader and your parent or guardian').save()
        RankRequirement(sort_order=51, number='3c', revision='2016', rank=second_class,
                        short_desc='Hiking Hazards',
                        description='Describe some hazards or injuries that you might encounter on your hike and what you can do to help prevent them.').save()
        RankRequirement(sort_order=52, number='3d', revision='2016', rank=second_class,
                        short_desc='Day/Night Directions',
                        description='Demonstrate how to find directions during the day and at night without using a compass or an electronic device').save()
        RankRequirement(sort_order=53, number='', is_header=True,
                        header='Nature:', rank=second_class, revision='2016').save()
        RankRequirement(sort_order=54, number='4', revision='2016', rank=second_class,
                        short_desc='Identify 10 wild animals',
                        description='Identify or show evidence of at least 10 kinds of wild animals (such as birds, mammals, reptiles, fish, or mollusks) found in your local area or camping location. You may show evidence by tracks, signs, or photographs you have taken.').save()
        RankRequirement(sort_order=55, number='', is_header=True,
                        header='Aquatics:', rank=second_class, revision='2016').save()
        RankRequirement(sort_order=56, number='5a', revision='2016', rank=second_class,
                        short_desc='Safe Swim',
                        description='Tell what precautions must be taken for a safe swim.').save()
        RankRequirement(sort_order=57, number='5b', revision='2016', rank=second_class,
                        short_desc='BSA Beginner Swim Test',
                        description='Demonstrate your ability to pass the BSA beginner test: Jump feetfirst into water over your head in depth, level off and swim 25 feet on the surface, stop, turn sharply, resume swimming, then return to your starting place.').save()
        RankRequirement(sort_order=58, number='5c', revision='2016', rank=second_class,
                        short_desc='Water Rescue',
                        description='Demonstrate water rescue methods by reaching with your arm or leg, by reaching with a suitable object, and by throwing lines and objects.').save()
        RankRequirement(sort_order=59, number='5d', revision='2016', rank=second_class,
                        short_desc='Water Rescue Ins and Outs',
                        description='Explain why swimming rescues should not be attempted when a reaching or throwing rescue is possible. Explain why and how a rescue swimmer should avoid contact with the victim.').save()
        RankRequirement(sort_order=60, number='', is_header=True,
                        header='First Aid and Emergency Preparedness:', rank=second_class, revision='2016').save()
        RankRequirement(sort_order=61, number='6a', revision='2016', rank=second_class,
                        short_desc='1st Aid',
                        description="""Demonstrate first aid for the following:
                            Object in the eye
                            Bite of a warm-blooded animal
                            Puncture wounds from a splinter, nail, and fishhook
                            Serious burns (partial thickness, or second-degree)
                            Heat exhaustion
                            Shock
                            Heatstroke, dehydration, hypothermia, and hyperventilation""").save()
        RankRequirement(sort_order=62, number='6b', revision='2016', rank=second_class,
                        short_desc='Stopped Breathing',
                        description='Show what to do for “hurry” cases of stopped breathing, stroke, severe bleeding, and ingested poisoning.').save()
        RankRequirement(sort_order=63, number='6c', revision='2016', rank=second_class,
                        short_desc='Reduce Injuries',
                        description='Tell what you can do while on a campout or hike to prevent or reduce the occurrence of the injuries listed in Second Class requirements 6a and 6b.').save()
        RankRequirement(sort_order=64, number='6d', revision='2016', rank=second_class,
                        short_desc='Emergency Response',
                        description='Explain what to do in case of accidents that require emergency response in the home and backcountry. Explain what constitutes an emergency and what information you will need to provide to a responder.').save()
        RankRequirement(sort_order=65, number='6e', revision='2016', rank=second_class,
                        short_desc='Car Accident',
                        description='Tell how you should respond if you come upon the scene of a vehicular accident.').save()
        RankRequirement(sort_order=66, number='', is_header=True,
                        header=':', rank=second_class, revision='2016').save()
        RankRequirement(sort_order=67, number='7a', revision='2016', rank=second_class,
                        short_desc='Physically Active',
                        description=' After completing Tenderfoot requirement 6c, be physically active at least 30 minutes each day for five days a week for four weeks. Keep track of your activities.').save()
        RankRequirement(sort_order=68, number='7b', revision='2016', rank=second_class,
                        short_desc='Physically Active Goals',
                        description='Share your challenges and successes in completing Second Class requirement 7a. Set a goal for continuing to include physical activity as part of your daily life and develop a plan for doing so.').save()
        RankRequirement(sort_order=69, number='7c', revision='2016', rank=second_class,
                        short_desc='Drug/Alcohol Dangers',
                        description='Participate in a school, community, or troop program on the dangers of using drugs, alcohol, and tobacco and other practices that could be harmful to your health. Discuss your participation in the program with your family, and explain the dangers of substance addictions. Report to your Scoutmaster or other adult leader in your troop about which parts of the Scout Oath and Scout Law relate to what you learned.').save()
        RankRequirement(sort_order=70, number='', is_header=True,
                        header='Citizenship:', rank=second_class, revision='2016').save()
        RankRequirement(sort_order=71, number='8a', revision='2016', rank=second_class,
                        short_desc='Flag Ceremony',
                        description='Participate in a flag ceremony for your school, religious institution, chartered organization, community, or Scouting activity.').save()
        RankRequirement(sort_order=72, number='8b', revision='2016', rank=second_class,
                        short_desc='Flag Respect',
                        description='Explain what respect is due the flag of the United States.').save()
        RankRequirement(sort_order=73, number='8c', revision='2016', rank=second_class,
                        short_desc='Save Money',
                        description='With your parents or guardian, decide on an amount of money that you would like to earn, based on the cost of a specific item you would like to purchase. Develop a written plan to earn the amount agreed upon and follow that plan; it is acceptable to make changes to your plan along the way. Discuss any changes made to your original plan and whether you met your goal.').save()
        RankRequirement(sort_order=74, number='8d', revision='2016', rank=second_class,
                        short_desc='Deal Shopping',
                        description='At a minimum of three locations, compare the cost of the item for which you are saving to determine the best place to purchase it. After completing Second Class requirement 8c, decide if you will use the amount that you earned as originally intended, save all or part of it, or use it for another purpose.').save()
        RankRequirement(sort_order=75, number='8e', revision='2016', rank=second_class,
                        short_desc='2 Service Hours',
                        description='Participate in two hours of service through one or more service projects approved by your Scoutmaster. Explain how your service to others relates to the Scout Oath.').save()
        RankRequirement(sort_order=76, number='', is_header=True,
                        header='Personal Safety Awareness:', rank=second_class, revision='2016').save()
        RankRequirement(sort_order=77, number='9a', revision='2016', rank=second_class,
                        short_desc='3r Personal Safety',
                        description='Explain the three R’s of personal safety and protection.').save()
        RankRequirement(sort_order=78, number='9b', revision='2016', rank=second_class,
                        short_desc='Bullying',
                        description='Describe bullying; tell what the appropriate response is to someone who is bullying you or another person.').save()
        RankRequirement(sort_order=79, number='', is_header=True,
                        header='Scout Spirit:', rank=second_class, revision='2016').save()
        RankRequirement(sort_order=80, number='10', revision='2016', rank=second_class,
                        short_desc='Scout Spirit/Duty to God',
                        description=' Demonstrate Scout spirit by living the Scout Oath and Scout Law. Tell how you have done your duty to God and how you have lived four different points of the Scout Law (not to include those used for Tenderfoot requirement 9) in your everyday life.').save()
        RankRequirement(sort_order=81, number='11', revision='2016', rank=second_class,
                        short_desc='Scoutmaster Conference',
                        description='While working toward the Second Class rank, and after completing Tenderfoot requirement 10, participate in a Scoutmaster conference.').save()
        RankRequirement(sort_order=82, number='12', revision='2016', rank=second_class,
                        short_desc='Board of Review',
                        description='Successfully complete your board of review for the Second Class rank.').save()

        print('Loading RankRequirement for First Class')
        RankRequirement(sort_order=83, number='', is_header=True,
                        header='Camping and Outdoor Ethics:', rank=first_class, revision='2016').save()
        RankRequirement(sort_order=84, number='1a', revision='2016', rank=first_class,
                        short_desc='10 Activities (6 nights camping)',
                        description='Since joining Boy Scouts, participate in 10 separate troop/patrol activities, at least six of which must be held outdoors. Of the outdoor activities, at least three must include overnight camping. These activities do not include troop or patrol meetings. On campouts, spend the night in a tent that you pitch or other structure that you help erect, such as a lean-to, snow cave, or tepee.').save()
        RankRequirement(sort_order=85, number='1b', revision='2016', rank=first_class,
                        short_desc='Tread Lightly!',
                        description='Explain each of the principles of Tread Lightly! and tell how you practiced them on a campout or outing. This outing must be different from the ones used for Tenderfoot requirement 1c and Second Class requirement 1b.').save()
        RankRequirement(sort_order=86, number='', is_header=True,
                        header='Cooking:', rank=first_class, revision='2016').save()
        RankRequirement(sort_order=87, number='2a', revision='2016', rank=first_class,
                        short_desc='Plan Menu',
                        description='Help plan a menu for one of the above campouts that includes at least one breakfast, one lunch, and one dinner, and that requires cooking at least two of the meals. Tell how the menu includes the foods from MyPlate or the current USDA nutritional model and how it meets nutritional needs for the planned activity or campout.').save()
        RankRequirement(sort_order=88, number='2b', revision='2016', rank=first_class,
                        short_desc='Budget and Shop Menu',
                        description=' Using the menu planned in First Class requirement 2a, make a list showing a budget and the food amounts needed to feed three or more boys. Secure the ingredients.').save()
        RankRequirement(sort_order=89, number='2c', revision='2016', rank=first_class,
                        short_desc='Show Gear needed to Cook Menu',
                        description='Show which pans, utensils, and other gear will be needed to cook and serve these meals.').save()
        RankRequirement(sort_order=90, number='2d', revision='2016', rank=first_class,
                        short_desc='Safe food Handling',
                        description='Demonstrate the procedures to follow in the safe handling and storage of fresh meats, dairy products, eggs, vegetables, and other perishable food products. Show how to properly dispose of camp garbage, cans, plastic containers, and other rubbish.').save()
        RankRequirement(sort_order=91, number='2e', revision='2016', rank=first_class,
                        short_desc='Serve as Cook',
                        description='On one campout, serve as cook. Supervise your assistant(s) in using a stove or building a cooking fire. Prepare the breakfast, lunch, and dinner planned in First Class requirement 2a. Supervise the cleanup.').save()
        RankRequirement(sort_order=92, number='', is_header=True,
                        header='Tools:', rank=first_class, revision='2016').save()
        RankRequirement(sort_order=93, number='3a', revision='2016', rank=first_class,
                        short_desc='Lashing use',
                        description='Discuss when you should and should not use lashings.').save()
        RankRequirement(sort_order=94, number='3b', revision='2016', rank=first_class,
                        short_desc='Timber & Clove Hitch',
                        description='Demonstrate tying the timber hitch and clove hitch.').save()
        RankRequirement(sort_order=95, number='3c, revision='2016', rank=first_class,
                        short_desc='Demo Lashings',
                        description='Demonstrate tying the square, shear, and diagonal lashings by joining two or more poles or staves together.').save()
        RankRequirement(sort_order=96, number='3d', revision='2016', rank=first_class,
                        short_desc='Useful Camp Gadget',
                        description='Use lashings to make a useful camp gadget or structure.').save()
        RankRequirement(sort_order=97, number='', is_header=True,
                        header='Navigation:', rank=first_class, revision='2016').save()
        RankRequirement(sort_order=98, number='4a', revision='2016', rank=first_class,
                        short_desc='Map/Compass Orienteering',
                        description='Using a map and compass, complete an orienteering course that covers at least one mile and requires measuring the height and/or width of designated items (tree, tower, canyon, ditch, etc.).').save()
        RankRequirement(sort_order=99, number='4b', revision='2016', rank=first_class,
                        short_desc='GPS Orienteering',
                        description=' Demonstrate how to use a handheld GPS unit, GPS app on a smartphone, or other electronic navigation system. Use GPS to find your current location, a destination of your choice, and the route you will take to get there. Follow that route to arrive at your destination.').save()
        RankRequirement(sort_order=100, number='', is_header=True,
                        header='Nature:', rank=first_class, revision='2016').save()
        RankRequirement(sort_order=101, number='5a', revision='2016', rank=first_class,
                        short_desc='10 Native Plants',
                        description='Identify or show evidence of at least 10 kinds of native plants found in your local area or campsite location. You may show evidence by identifying fallen leaves or fallen fruit that you find in the field, or as part of a collection you have made, or by photographs you have taken.').save()
        RankRequirement(sort_order=102, number='5b', revision='2016', rank=first_class,
                        short_desc='Weather Forecast',
                        description=' Identify two ways to obtain a weather forecast for an upcoming activity. Explain why weather forecasts are important when planning for an event.').save()
        RankRequirement(sort_order=103, number='5c', revision='2016', rank=first_class,
                        short_desc='Hazardous Weather',
                        description='Describe at least three natural indicators of impending hazardous weather, the potential dangerous events that might result from such weather conditions, and the appropriate actions to take.').save()
        RankRequirement(sort_order=104, number='5d', revision='2016', rank=first_class,
                        short_desc='Local Extreme Weather',
                        description='Describe extreme weather conditions you might encounter in the outdoors in your local geographic area. Discuss how you would determine ahead of time the potential risk of these types of weather dangers, alternative planning considerations to avoid such risks, and how you would prepare for and respond to those weather conditions.').save()
        RankRequirement(sort_order=105, number='', is_header=True,
                        header='Aquatics:', rank=first_class, revision='2016').save()
        RankRequirement(sort_order=106, number='6a', revision='2016', rank=first_class,
                        short_desc='BSA Swim Test',
                        description='Successfully complete the BSA swimmer test').save()
        RankRequirement(sort_order=107, number='6b', revision='2016', rank=first_class,
                        short_desc='Safe Trip Afloat',
                        description='Tell what precautions must be taken for a safe trip afloat.').save()
        RankRequirement(sort_order=108, number='6c', revision='2016', rank=first_class,
                        short_desc='Watercraft Parts Identification',
                        description='Identify the basic parts of a canoe, kayak, or other boat. Identify the parts of a paddle or an oar.').save()
        RankRequirement(sort_order=109, number='6d', revision='2016', rank=first_class,
                        short_desc='Watercraft Proper Body Positioning',
                        description='Describe proper body positioning in a watercraft, depending on the type and size of the vessel. Explain the importance of proper body position in the boat.').save()
        RankRequirement(sort_order=110, number='6e', revision='2016', rank=first_class,
                        short_desc='Line Water Rescue',
                        description='With a helper and a practice victim, show a line rescue both as tender and as rescuer. (The practice victim should be approximately 30 feet from shore in deep water.)').save()
        RankRequirement(sort_order=111, number='', is_header=True,
                        header='First Aid and Emergency Preparedness:', rank=first_class, revision='2016').save()
        RankRequirement(sort_order=112, number='7a', revision='2016', rank=first_class,
                        short_desc='Sprains/Head/Arm/Collar Bone',
                        description='Demonstrate bandages for a sprained ankle and for injuries on the head, the upper arm, and the collarbone.').save()
        RankRequirement(sort_order=113, number='7b', revision='2016', rank=first_class,
                        short_desc='Transport Injured Person',
                        description="""By yourself and with a partner, show how to:
                            Transport a person from a smoke-filled room.
                            Transport for at least 25 yards a person with a sprained ankle.""").save()
        RankRequirement(sort_order=114, number='7c', revision='2016', rank=first_class,
                        short_desc='5 Signs Heart Attack',
                        description='Tell the five most common signals of a heart attack. Explain the steps (procedures) in cardiopulmonary resuscitation (CPR).').save()
        RankRequirement(sort_order=115, number='7d', revision='2016', rank=first_class,
                        short_desc='Dangers of Local Utilities',
                        description='Tell what utility services exist in your home or meeting place. Describe potential hazards associated with these utilities and tell how to respond in emergency situations.').save()
        RankRequirement(sort_order=116, number='7e', revision='2016', rank=first_class,
                        short_desc='Emergency Action Plan',
                        description='Develop an emergency action plan for your home that includes what to do in case of fire, storm, power outage, and water outage.').save()
        RankRequirement(sort_order=117, number='7f', revision='2016', rank=first_class,
                        short_desc='Potable Water',
                        description='Explain how to obtain potable water in an emergency.').save()
        RankRequirement(sort_order=118, number='', is_header=True,
                        header='Fitness:', rank=first_class, revision='2016').save()
        RankRequirement(sort_order=119, number='8a', revision='2016', rank=first_class,
                        short_desc='Physically Active',
                        description='After completing Second Class requirement 7a, be physically active at least 30 minutes each day for five days a week for four weeks. Keep track of your activities.').save()
        RankRequirement(sort_order=120, number='8b', revision='2016', rank=first_class,
                        short_desc='Physical Activity Goals',
                        description='Share your challenges and successes in completing First Class requirement 8a. Set a goal for continuing to include physical activity as part of your daily life.').save()
        RankRequirement(sort_order=121, number='', is_header=True,
                        header='Citizenship:', rank=first_class, revision='2016').save()
        RankRequirement(sort_order=122, number='9a', revision='2016', rank=first_class,
                        short_desc='Obligations of US Citizen',
                        description='Visit and discuss with a selected individual approved by your leader (for example, an elected official, judge, attorney, civil servant, principal, or teacher) the constitutional rights and obligations of a U.S. citizen.').save()
        RankRequirement(sort_order=123, number='9b', revision='2016', rank=first_class,
                        short_desc='Local Environmental Issue',
                        description='Investigate an environmental issue affecting your community. Share what you learned about that issue with your patrol or troop. Tell what, if anything, could be done by you or your community to address the concern.').save()
        RankRequirement(sort_order=124, number='9c', revision='2016', rank=first_class,
                        short_desc='Reduce/Recycle/Reuse',
                        description='On a Scouting or family outing, take note of the trash and garbage you produce. Before your next similar outing, decide how you can reduce, recycle, or repurpose what you take on that outing, and then put those plans into action. Compare your results.').save()
        RankRequirement(sort_order=125, number='9d', revision='2016', rank=first_class,
                        short_desc='3 Service Hours',
                        description='Participate in three hours of service through one or more service projects approved by your Scoutmaster. The project(s) must not be the same service project(s) used for Tenderfoot requirement 7b and Second Class requirement 8e. Explain how your service to others relates to the Scout Law.').save()
        RankRequirement(sort_order=126, number='', is_header=True,
                        header='Leadership:', rank=first_class, revision='2016').save()
        RankRequirement(sort_order=127, number='10', revision='2016', rank=first_class,
                        short_desc='Invite Friend',
                        description='Tell someone who is eligible to join Boy Scouts, or an inactive Boy Scout, about your Scouting activities. Invite him to an outing, activity, service project, or meeting. Tell him how to join, or encourage the inactive Boy Scout to become active. Share your efforts with your Scoutmaster or other adult leader.').save()
        RankRequirement(sort_order=128, number='', is_header=True,
                        header='Scout Spirit:', rank=first_class, revision='2016').save()
        RankRequirement(sort_order=129, number='11', revision='2016', rank=first_class,
                        short_desc='Scout Oath/Law/God',
                        description='Demonstrate Scout spirit by living the Scout Oath and Scout Law. Tell how you have done your duty to God and how you have lived four different points of the Scout Law (different from those points used for previous ranks) in your everyday life.').save()
        RankRequirement(sort_order=130, number='12', revision='2016', rank=first_class,
                        short_desc='Scoutmaster Conference',
                        description='While working toward the First Class rank, and after completing Second Class requirement 11, participate in a Scoutmaster conference.').save()
        RankRequirement(sort_order=131, number='13', revision='2016', rank=first_class,
                        short_desc='Board of Review',
                        description='Successfully complete your board of review for the First Class rank.').save()

        print('Loading RankRequirement for Star')

    def handle(self, *args, **options):
        self._create_base_data()
