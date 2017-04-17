**This documentation is automatically generated.**

**Output schemas only represent `data` and not the full output; see output examples and the JSend specification.**

# /api/summarize/?

    Content-Type: application/json

## POST


**Input Schema**
```json
{
    "properties": {
        "text": {
            "type": "string"
        },
        "word_count": {
            "type": "number"
        }
    },
    "type": "object"
}
```


**Input Example**
```json
{
    "text": "Thomas A. Anderson is a man living two lives. By day he is an average computer programmer and by night a hacker known as Neo. Neo has always questioned his reality, but the truth is far beyond his imagination. Neo finds himself targeted by the police when he is contacted by Morpheus, a legendary computer hacker branded a terrorist by the government. Morpheus awakens Neo to the real world, a ravaged wasteland where most of humanity have been captured by a race of machines that live off of the humans' body heat and electrochemical energy and who imprison their minds within an artificial reality known as the Matrix. As a rebel against the machines, Neo must return to the Matrix and confront the agents: super-powerful computer programs devoted to snuffing out Neo and the entire human rebellion.",
    "word_count": 50
}
```


**Output Schema**
```json
{
    "properties": {
        "data": {
            "type": "object"
        },
        "status": {
            "type": "string"
        }
    },
    "type": "object"
}
```


**Output Example**
```json
{
    "data": {
        "summary": "Morpheus awakens Neo to the real world, a ravaged wasteland where most of humanity have been captured by a race of machines that live off of the humans' body heat and electrochemical energy and who imprison their minds within an artificial reality known as the Matrix."
    },
    "status": "success"
}
```


**Notes**

POST the required parameters
* `text`: text to be summarized
* `word_count`: summarized text word count


