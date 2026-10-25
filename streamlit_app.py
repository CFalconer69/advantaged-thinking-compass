
import streamlit as st

st.set_page_config(
    page_title="Advantaged Thinking Development Compass",
    page_icon="🧭",
    layout="centered",
)

st.title("🧭 The Development Compass")
st.caption("An Advantaged Thinking resource finder for practitioners")

st.write(
    "Start with what matters to the young person. Explore one or more "
    "areas together, then find relevant resources, tools and possible "
    "curriculum activities."
)

st.info(
    "The Compass is a flexible signposting tool, not an assessment. "
    "It does not score, diagnose or categorise young people."
)

# Resource directory.
# Curriculum links are provisional and must be checked against
# the original session instructions before being relied upon.

resources = {
    "Identity and direction": {
        "signposts": [
            "Strengths",
            "What's Good?",
            "Direction",
        ],
        "tools": [
            "Advantage Map",
            "Direction Compass — Week 13",
            "10% Move",
        ],
        "sessions": (
            "Potential links: Weeks 1, 6 and 11–13. "
            "Check the original session purposes before selecting."
        ),
    },
    "Confidence and navigating challenges": {
        "signposts": [
            "Confidence",
            "Feeling Stuck",
            "Pause and Reset",
            "Keep Going",
        ],
        "tools": [
            "When You Forget — Week 17",
            "Pause and Reset",
            "10% Move",
        ],
        "sessions": (
            "Potential links: Weeks 17, 20, 24–25, 46 or 51, "
            "depending on the situation. Verify the original content."
        ),
    },
    "Voice, influence, relationships and belonging": {
        "signposts": [
            "Using My Voice",
            "Staying Involved",
            "Who's In Your Corner?",
        ],
        "tools": [
            "Voice Ladder",
            "Peer Mediation Platform",
            "Communal Space Accord",
            "Mapping Social Capital",
        ],
        "sessions": (
            "Potential links: Weeks 27–30 and 35–38. "
            "Check the session purpose and whether organisational "
            "change is also needed."
        ),
    },
    "Transitions and practical independence": {
        "signposts": [
            "Direction",
            "Who's In Your Corner?",
            "Keep Going",
        ],
        "tools": [
            "Mapping Sustainable Networks — Week 41",
            "Autonomy Budget Matrix — Week 43",
            "Emergency Reset Routine — Week 46",
            "Independent Return Path — Week 51",
        ],
        "sessions": (
            "Potential links: Weeks 40–43 and 46–52, "
            "depending on the goal. Verify the original session content."
        ),
    },
}

st.header("1. What matters to the young person?")

goal = st.text_area(
    "What have they said they want to explore, change, understand or achieve?",
    placeholder="Use their own words where possible. A broad hope or uncertainty is fine.",
    height=100,
)

st.caption(
    "Use fictional examples while testing. Avoid entering names or "
    "identifiable personal information."
)

st.header("2. Is anything urgent?")

urgent = st.radio(
    "Does an immediate safety concern or urgent practical need require attention?",
    [
        "No immediate concern identified",
        "Yes — urgent support may be needed",
        "I'm not sure",
    ],
    index=None,
)

if urgent in ["Yes — urgent support may be needed", "I'm not sure"]:
    st.warning(
        "Prioritise appropriate safeguarding, specialist or practical support. "
        "Follow your organisation's procedures. Do not delay necessary help "
        "to complete this tool."
    )

st.header("3. Which areas might be relevant?")

st.caption(
    "Select as many as seem useful. These areas overlap and are not "
    "stages or labels."
)

areas = st.multiselect(
    "Areas to explore",
    list(resources.keys()),
)

st.header("4. What kind of help might be useful?")

help_types = st.multiselect(
    "Select any that apply",
    [
        "Understand something or reflect",
        "Recognise strengths and interests",
        "Practise a skill or try an activity",
        "Find a supportive person or relationship",
        "Access an opportunity",
        "Have a voice or influence a decision",
        "Prepare for a transition",
        "Address a practical barrier",
        "Build trust before exploring goals",
    ],
)

st.divider()

if st.button("Find relevant resources", type="primary"):
    if urgent is None:
        st.warning("Please complete the urgent-needs check first.")

    elif urgent != "No immediate concern identified":
        st.warning(
            "Address the urgent concern or seek appropriate advice first. "
            "You can return to resource signposting when appropriate."
        )

    elif not goal.strip():
        st.warning(
            "Start with the young person's priority, in their own words "
            "where possible. A broad aspiration or uncertainty is enough."
        )

    elif not areas and not help_types:
        st.warning(
            "Select at least one development area or type of help "
            "to find relevant resources."
        )

    else:
        st.header("Your resource guide")

        st.markdown("**Starting point**")
        st.write(goal)

        if areas:
            st.subheader("Relevant development areas")

            for area in areas:
                item = resources[area]

                with st.expander(area, expanded=True):
                    st.markdown("**Built for More signposts to explore**")
                    for signpost in item["signposts"]:
                        st.markdown(f"- {signpost}")

                    st.markdown("**Named tools and resources**")
                    for tool in item["tools"]:
                        st.markdown(f"- {tool}")

                    st.markdown("**Possible curriculum connections**")
                    st.write(item["sessions"])

        if help_types:
            st.subheader("What kind of response might help?")

            for help_type in help_types:
                st.markdown(f"- {help_type}")

            if "Address a practical barrier" in help_types:
                st.info(
                    "Consider whether practical assistance or action by "
                    "the organisation is needed, rather than a curriculum "
                    "activity alone."
                )

            if "Have a voice or influence a decision" in help_types:
                st.info(
                    "Consider whether the practitioner or organisation "
                    "needs to change how it listens, shares power or "
                    "responds to the young person's views."
                )

        st.divider()
        st.markdown("### Choosing what to use")

        st.write(
            "Use these results as options to explore together, not as "
            "instructions or a prescribed pathway. Choose the resource "
            "that best fits the young person's wishes and circumstances. "
            "It is fine to choose none of them or to start somewhere else."
        )

        st.caption(
            "Curriculum connections are provisional navigation suggestions, "
            "not verified recommendations. Check each original session's "
            "purpose and instructions before use."
        )

st.divider()

st.caption(
    "Prototype only. Entries are not saved to a database. "
    "This tool does not replace professional judgement, safeguarding "
    "procedures or access to practical support."
)

