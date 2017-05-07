import config
import urls
import os
cwd = os.getcwd()
print cwd

if __name__ == "__main__":
    config.app.run(debug=True)