from pathlib import Path
import re

path = Path('data/tryouts.yaml')
if not path.exists():
    raise SystemExit('data/tryouts.yaml not found. Run from the repo root.')

text = path.read_text()

new_faqs = '''faqs:
  - question: "How do I register?"
    answer: "Use the Become a Tiger registration link on this page. After the form is submitted, a Rawlings Tigers NOVA coach or program contact will follow up with next steps."
  - question: "How many sessions does my player need to attend?"
    answer: "Players only need to attend one tryout session. A player may attend a make-up session if they are unavailable or if a tryout is canceled due to weather."
  - question: "What should players bring?"
    answer: "Players should bring a glove, bat, helmet, cleats or turf shoes, and a water bottle. Catchers should bring their catching gear if they have it."
  - question: "What ages are eligible?"
    answer: "Rawlings Tigers NOVA hosts tryouts for rising 10U through 14U players, depending on season roster needs and team openings. Use the age chart on this page to confirm the correct age group."
  - question: "How do I determine which age group my player falls into?"
    answer: "Use the expandable age chart in the Schedule Dates section as a quick reference before registering. If you are unsure, submit the player information and the staff can help confirm the correct age group."
  - question: "Where are Rawlings Tigers NOVA travel baseball tryouts held?"
    answer: "Tryout locations vary by age group and session. Rawlings Tigers NOVA serves players across Northern Virginia, including Woodbridge, Dumfries, Montclair, Dale City, Stafford, Manassas, Fairfax, Prince William County, and nearby communities."
  - question: "What age groups does Rawlings Tigers NOVA offer travel baseball tryouts for?"
    answer: "Rawlings Tigers NOVA typically offers travel baseball tryouts for rising 10U, 11U, 12U, 13U, and 14U players, depending on season roster needs and team openings."
  - question: "What makes Rawlings Tigers NOVA different from other Northern Virginia travel baseball teams?"
    answer: "The program emphasizes professional coaching, structured player development, competitive schedules, baseball IQ, accountability, and team culture. Players are evaluated on skills, effort, attitude, and readiness to compete at a high level."
  - question: "What if I can’t attend the posted dates?"
    answer: "Private tryouts may be available upon request. Contact Rawlings Tigers NOVA with your player’s age group, baseball background, and availability so a coach can follow up."
  - question: "How will I know if I made the team?"
    answer: "Players are typically notified by email within a few days of their tryout. Coaches will provide next-step details for roster invitations, follow-up evaluations, or future opportunities."
  - question: "Will pitchers and catchers be evaluated separately?"
    answer: "Position-specific evaluation work may follow the main session when appropriate. Pitchers and catchers should be prepared for additional throwing, receiving, or position-specific review if requested by the coaches."
  - question: "Do players need prior travel baseball experience?"
    answer: "Prior travel baseball experience can help, but it is not the only factor. Coaches look at skill level, athleticism, coachability, effort, attitude, baseball IQ, and readiness for a competitive team environment."
'''

if re.search(r'(?m)^faqs:\s*$', text):
    # Replace faqs block until next top-level YAML key or EOF.
    text = re.sub(r'(?ms)^faqs:\s*\n.*?(?=^[A-Za-z0-9_]+:\s*|\Z)', new_faqs + '\n', text, count=1)
else:
    text = text.rstrip() + '\n\n' + new_faqs + '\n'

path.write_text(text)
print('Updated data/tryouts.yaml FAQ entries.')
print('Run: hugo server -D --disableFastRender')
