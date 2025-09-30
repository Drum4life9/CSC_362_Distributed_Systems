from flask import Flask, Response
from flask_hal import link
from flask_hal.document import Document, Embedded
from flask_hal.link import Link, Collection

app = Flask(__name__)

@app.route('/queue')
def doc():
    hal_doc = Document(
        embedded={
            'user': Embedded(
                data={
                    'id': 102,
                    'email': 'brainmyres691@fmail.co',
                    'name': 'Brain Myres',
                },
                links=Collection(Link('self', '/users/102'))
            ),
            'queue': Collection(
                Link('self', '/games/503'),
                Link('self', '/games/301')
            )
        }
    )

    return Response(hal_doc.to_json(), mimetype='application/hal+json')

if __name__ == "__main__":
    app.run(debug=True)
