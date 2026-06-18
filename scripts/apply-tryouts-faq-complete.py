from pathlib import Path
import yaml

path = Path("data/tryouts.yaml")
if not path.exists():
    raise SystemExit("data/tryouts.yaml not found. Run from the repo root.")

data = yaml.safe_load(path.read_text()) or {}

data["faqs"] = [
    {
        "question": "How do I register?",
        "answer": "Use the Become a Tiger registration link on this page to submit your player information. A Rawlings Tigers NOVA coach or program contact will follow up with the next steps."
    },
    {
        "question": "How many sessions does my player need to attend?",
        "answer": "Players only need to attend one open evaluation date. A player may attend a make-up session if they are unavailable, if a session is canceled due to weather, or if a coach requests a follow-up."
    },
    {
        "question": "What should players bring?",
        "answer": "Players should bring a glove, bat, helmet, cleats or turf shoes, water bottle, and any position-specific gear they normally use. Catchers should bring catcher’s gear when available."
    },
    {
        "question": "What ages are eligible?",
        "answer": "Rawlings Tigers NOVA typically hosts tryouts for rising 10U, 11U, 12U, 13U, and 14U players, depending on roster needs and available openings by season."
    },
    {
        "question": "How do I determine which age group my player falls into?",
        "answer": "Use the player age chart in the Schedule Dates section to confirm the correct rising age group before registering. Age groups are based on the player’s birth date range for the listed season."
    },
    {
        "question": "Where are Rawlings Tigers NOVA travel baseball tryouts held?",
        "answer": "Tryout locations may vary by age group and session. Rawlings Tigers NOVA serves players across Northern Virginia, including Woodbridge, Dumfries, Montclair, Dale City, Stafford, Manassas, Fairfax, Prince William County, and nearby communities."
    },
    {
        "question": "What age groups does Rawlings Tigers NOVA offer travel baseball tryouts for?",
        "answer": "Rawlings Tigers NOVA offers travel baseball tryouts for multiple age groups, typically including rising 10U, 11U, 12U, 13U, and 14U players depending on team openings and roster needs."
    },
    {
        "question": "What makes Rawlings Tigers NOVA different from other Northern Virginia travel baseball teams?",
        "answer": "The program emphasizes structured player development, professional coaching, competitive schedules, baseball IQ, accountability, effort, attitude, and team culture. Players are evaluated on both skill and readiness to compete in a team-first environment."
    },
    {
        "question": "What if I can’t attend the posted dates?",
        "answer": "Private tryouts may be available by request. If your player cannot attend the posted dates, contact Rawlings Tigers NOVA so a coach can review availability and determine whether a private evaluation or make-up session is possible."
    },
    {
        "question": "How will I know if I made the team?",
        "answer": "Players are typically contacted by email within a few days of their tryout. Coaches will provide next-step details for roster invitations, follow-up sessions, or additional evaluation needs."
    },
]

# Keep YAML readable.
path.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=120))
print(f"Updated {path} with {len(data['faqs'])} complete FAQ items.")
