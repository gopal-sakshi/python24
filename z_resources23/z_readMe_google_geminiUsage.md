google gemini api key rate limits

`Metric                      What it means                   Free Tier Limit (Approx)`
RPM (Requests Per Minute)   How many times you can call the API in 60 seconds               15 RPM (Flash models)
RPD (Requests Per Day)      Your total budget for the day                                   1,000 RPD
TPM (Tokens Per Minute)     The total volume of words/data sent and received per minute     1 million TPM


In AI, we don't count words; we count Tokens.

- 1 Token       ≈ 4 characters (in English)
- 100 Tokens    ≈ 400 characters (or) 75 words

Images/Video: These are converted into "token equivalents." For example, a standard image might cost about 258 tokens.


LangGraph works by sending the entire conversation history back to the AI every time a new step happens.
Step 1: 500 tokens.
Step 2: 500 (old) + 500 (new) = 1,000 tokens.
Step 3: 1,000 (old) + 500 (new) = 1,500 tokens.

This "snowball effect" is why the 1 million TPM limit is actually very helpful—it gives you plenty of room for complex agents.


<!-- ******************************************************************************** -->