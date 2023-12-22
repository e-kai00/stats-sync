import os
from statsapp import app


if __name__ == "__main__":
    app.run(debug=os.environ.get("DEBUG"))
    