import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

import streamlit as st

st.set_page_config(
    page_title="Advantaged Thinking Development Compass",
    page_icon="🧭",
    layout="centered",
)

st.title("🧭 The Development Compass")
st.subheader("An Advantaged Thinking practitioner tool")

st.write(
    "Start with the young person's own words. "
    "Explore what matters to them, consider what support might help, "
    "and agree a next step together."
)

st.info(
    "This is an early prototype. It supports conversation and practitioner "
    "judgement; it is not a diagnostic or scoring tool."
)

st.divider()

st.header("1. Start with the young person's words")

young_person_words = st.text_area(
    "What has the young person said they want, hope for, "
    "are worried about, or would like to change?",
    placeholder="Use their own words where possible. Avoid names or identifying details.",
    height=120,
)

st.caption(
    "You can use a fictional example while testing. "
    "This prototype does not save entries to a database."
)

st.header("2. Check what needs attention first")

urgent_need = st.radio(
    "Is there an immediate safety concern or urgent practical need "
    "that must be addressed before curriculum activities?",
    [
        "No immediate concern identified",
        "Yes — urgent support or safeguarding action may be needed",
        "Not sure — I need to explore this further",
    ],
    index=None,
)

if urgent_need in [
    "Yes — urgent support or safeguarding action may be needed",
    "Not sure — I need to explore this further",
]:
    st.warning(
        "Pause curriculum signposting. Follow your organisation's "
        "safeguarding and urgent-support procedures, consult the appropriate "
        "colleague, and address immediate practical needs. The Compass "
        "must never delay necessary support."
    )

st.header("3. What would be helpful to explore?")

st.write(
    "Choose the area that seems most relevant to the young person now. "
    "This is a conversation starter, not a label. More than one area may apply."
)


areas = st.multiselect(
    "Possible development areas — select all that seem relevant",
    [
        "Identity and direction",
        "Confidence and navigating challenges",
        "Voice, influence and belonging",
        "Transitions and independence",
        "I'm not sure yet",
    ],
    help=(
        "More than one area can be relevant. "
        "Explore these together with the young person rather than "
        "treating them as fixed categories."
    ),
)


help_needed = st.multiselect(
    "What kind of help might the young person want?",
    [
        "Recognising strengths and interests",
        "Exploring hopes and possible directions",
        "Working through a challenge or setback",
        "Building supportive relationships",
        "Being heard or influencing a decision",
        "Finding an opportunity or new experience",
        "Preparing for a change or transition",
        "Practical help with an immediate need",
        "Building trust before setting goals",
        "Something else",
    ],
)

st.header("4. Explore together")

prompts = {
    "Identity and direction": [
        "What matters to you, even if you are not sure what comes next?",
        "When have you felt interested, capable or more like yourself?",
        "What possibilities would you like to explore without committing to one yet?",
    ],
    "Confidence and navigating challenges": [
        "What has been getting in the way, and what would make things easier?",
        "What has helped you keep going or recover from a difficult moment before?",
        "What support would make the next step feel manageable?",
    ],
    "Voice, influence and belonging": [
        "Where would you like your views to be heard?",
        "Who listens to you, takes you seriously or could help you have influence?",
        "What would need to change for you to feel more involved or included?",
    ],
    "Transitions and independence": [
        "What change is coming up, and what are you looking forward to or concerned about?",
        "What would help you feel prepared?",
        "Who or what will you still be able to rely on when things change?",
    ],
    "I'm not sure yet": [
        "What feels most important to talk about today?",
        "Would it help to talk, explore possibilities, solve a practical problem or simply take some time?",
        "What would make this conversation useful for you?",
    ],
}

if area:
    st.markdown("**Possible conversation prompts**")
    for prompt in prompts[area]:
        st.markdown(f"- {prompt}")

st.header("5. Agree a next step")

next_step = st.text_area(
    "What has the young person chosen to explore or do next?",
    placeholder="Record an agreed action, opportunity, conversation or practical support.",
)

practitioner_action = st.text_area(
    "What will the practitioner or organisation do?",
    placeholder="For example, arrange a conversation, remove a barrier or explore an opportunity.",
)

review = st.text_input(
    "When will you review this together?",
    placeholder="For example, at the next meeting",
)


if st.button("Create conversation summary", type="primary"):
    if urgent_need is None:
        st.error("Please complete the immediate-needs check first.")
    elif not young_person_words.strip():
        st.error("Start by recording what the young person wants to discuss. A fictional example is fine for testing.")
    elif urgent_need != "No immediate concern identified":
        st.warning(
            "The priority is to follow appropriate safeguarding or urgent-support "
            "procedures. Do not use curriculum signposting to replace that response."
        )
    elif not areas:
        st.error("Choose one or more possible areas to explore.")
    else:
        st.success("Conversation summary created")

        st.markdown("### Starting point")
        st.write(young_person_words)

        st.markdown("### Area(s) to explore")
        for selected_area in areas:
            st.markdown(f"- {selected_area}")


        st.markdown("### Possible areas of support")
        if help_needed:
            for item in help_needed:
                st.markdown(f"- {item}")
        else:
            st.write("No support type selected yet.")

        st.markdown("### Agreed next step")
        st.write(next_step or "Not yet agreed")

        st.markdown("### Practitioner or organisational action")
        st.write(practitioner_action or "Not yet agreed")

        st.markdown("### Review")
        st.write(review or "To be agreed")

        st.caption(
            "This summary is displayed for the current session only. "
            "Copy it to an approved system if needed, following your "
            "organisation's privacy and information-handling policies."
        )

st.divider()

st.caption(
    "Development prototype — curriculum session recommendations have not "
    "yet been linked and verified against the original Built for More materials."
)
