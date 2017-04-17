import tornado
from tornado_json.requesthandlers import APIHandler
from tornado_json import schema
from gensim.summarization import summarize

class Summarize(APIHandler):

    @schema.validate(
        input_schema={
            "type": "object",
            "properties": {
                "text": {"type": "string"},
                "word_count": {"type": "number"}
            }
        },
        input_example={
            "text": "Thomas A. Anderson is a man living two lives. By day he is an average computer programmer and by night a hacker known as Neo. Neo has always questioned his reality, but the truth is far beyond his imagination. Neo finds himself targeted by the police when he is contacted by Morpheus, a legendary computer hacker branded a terrorist by the government. Morpheus awakens Neo to the real world, a ravaged wasteland where most of humanity have been captured by a race of machines that live off of the humans' body heat and electrochemical energy and who imprison their minds within an artificial reality known as the Matrix. As a rebel against the machines, Neo must return to the Matrix and confront the agents: super-powerful computer programs devoted to snuffing out Neo and the entire human rebellion.",
            "word_count": 50
            },
        output_schema={
            "type": "object",
            "properties": {
                "status": {"type": "string"},
                "data": {"type": "object"},
            }
        },
        output_example={
            "status": "success",
            "data": {
                "summary": "Morpheus awakens Neo to the real world, a ravaged wasteland where most of humanity have been captured by a race of machines that live off of the humans' body heat and electrochemical energy and who imprison their minds within an artificial reality known as the Matrix."
                }
        },
    )

    def post(self):
        """
        POST the required parameters
        * `text`: text to be summarized
        """
        tornado.log.enable_pretty_logging()
        data = tornado.escape.json_decode(self.request.body)
        summary = summarize(data['text'], word_count=data['word_count'])
        print data

        return {
            "summary": summary
        }

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Server", "Summarizer v0.1.0")
        self.set_header("Access-Control-Allow-Headers", 'DNT,X-CustomHeader,Keep-Alive,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type')
        self.set_header('Access-Control-Allow-Methods', 'POST, OPTIONS')

    def options(self):
        self.set_status(204)
        self.clear_header('Content-Type')
        self.finish()
