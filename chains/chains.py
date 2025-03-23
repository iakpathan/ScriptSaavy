from chains.linkedin_chain import generate_linkedin_content
from chains.youtube_chains import generate_youtube_vlog, generate_youtube_podcast
from chains.classifier import classify_topic
from langchain.schema import AIMessage


def get_chain_and_generate(topic, duration=None):
    """Detect content type and run the appropriate chain."""
    content_type = classify_topic(topic)

    if content_type == "linkedin":
        # ✅ Generate LinkedIn content - no duration required
        result = generate_linkedin_content(topic)

    elif content_type == "vlog":
        if not duration:
            raise ValueError("Duration is required for YouTube Vlog!")
        # ✅ Generate YouTube Vlog content
        result = generate_youtube_vlog(topic, duration)

    elif content_type == "podcast":
        if not duration:
            raise ValueError("Duration is required for YouTube Podcast!")
        # ✅ Generate YouTube Podcast content
        result = generate_youtube_podcast(topic, duration)

    else:
        raise ValueError("Invalid content type detected!")

    # ✅ Check and extract content correctly
    if isinstance(result, AIMessage):
        return result.content.strip()
    elif isinstance(result, str):
        return result.strip()
    else:
        raise ValueError("Invalid response format from content generation chain.")
