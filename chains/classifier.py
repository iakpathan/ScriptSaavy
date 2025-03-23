from langchain.schema import AIMessage

# Classification Logic
def classify_topic(topic):
    """Classify whether the topic is for LinkedIn or YouTube."""
    linkedin_keywords = ["achievement", "career", "milestone", "promotion", "networking", "leadership"]
    youtube_vlog_keywords = ["vlog", "lifestyle", "travel", "daily routine"]
    youtube_podcast_keywords = ["podcast", "discussion", "interview", "talk"]

    topic_lower = topic.lower()

    # ✅ Check for LinkedIn-related keywords
    if any(keyword in topic_lower for keyword in linkedin_keywords):
        return "linkedin"
    
    # ✅ Check for YouTube vlog-related keywords
    elif any(keyword in topic_lower for keyword in youtube_vlog_keywords):
        return "vlog"
    
    # ✅ Check for YouTube podcast-related keywords
    elif any(keyword in topic_lower for keyword in youtube_podcast_keywords):
        return "podcast"

    # ✅ Use LLM-based classification as a fallback if no keyword matches
    try:
        # Invoke the classification chain
        classification_result = classification_chain.invoke({"topic": topic})

        # ✅ Check and handle response correctly
        if isinstance(classification_result, AIMessage):
            return classification_result.content.strip().lower()
        elif isinstance(classification_result, str):
            return classification_result.strip().lower()
        else:
            raise ValueError("Invalid response format from classification chain.")

    except Exception as e:
        print(f"Classification failed: {e}")
        return "vlog"  # Default to vlog if classification fails
