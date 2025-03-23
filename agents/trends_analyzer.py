from pytrends.request import TrendReq # type: ignore

# Initialize Google Trends API
pytrends = TrendReq(hl="en-US", tz=360)

def get_trending_keywords(topic: str, region="US") -> list:
    """Fetch trending search queries related to a given topic."""
    try:
        # Build payload with specified keyword and region
        pytrends.build_payload([topic], cat=0, timeframe="now 1-d", geo=region, gprop="")
        
        # Get related queries
        related_queries = pytrends.related_queries()
        
        if topic in related_queries:
            top_queries = related_queries[topic]["top"]
            if top_queries is not None:
                # Return top 5 trending queries
                trending_keywords = top_queries["query"].tolist()[:5]
                return trending_keywords
        return ["No trending keywords found."]
    except Exception as e:
        return [f"Error fetching Google Trends: {str(e)}"]
 
