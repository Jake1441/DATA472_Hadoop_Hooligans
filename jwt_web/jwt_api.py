# https://jwt.io/
import time
import pathlib
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
sleep_timeout = 30

"""
Input for role is comma before end of span not necessary if only one role.

needs to be
"
<pre class=" CodeMirror-line " role="presentation"><span role="presentation" title="Subject (whom the token refers to)" style="padding-right: 0.1px;">{</span></pre>
<pre class=" CodeMirror-line " role="presentation"><span role="presentation" title="Subject (whom the token refers to)" style="padding-right: 0.1px;">"role":"db_user"</span></pre>
<pre class=" CodeMirror-line " role="presentation"><span role="presentation" title="Subject (whom the token refers to)" style="padding-right: 0.1px;">}</span></pre>
"

<pre class=" CodeMirror-line " role="presentation">
    <span role="presentation" style="padding-right: 0.1px;" title="Subject (whom the token refers to)">
    "sub": "1234567890",
    </span>
</pre>

Input for secret key is 
<input type="text" name="secret" value="your-256-bit-secret" data-tippy="" data-original-title="Weak secret!">
Input for role is

cm-jwt-header
cm-jwt-dot
cm-jwt-payload
cm-jwt-dot
cm-jwt-signature
"""

chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
file = "jwt-token.html"
path = os.path.abspath(file)
url = pathlib.Path(path).as_uri()

# test!
#url = "https://jwt.io/"

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
driver.get(url)

# driver.execute_script("""
#     var l = document.getElementsByClassName("js-payload")[0];
#     var l2 = l.getElementsByClassName("CodeMirror-code")[0];
#     //l2.parentNode.createElement = '<pre class=" CodeMirror-line " role="presentation"><span role="presentation" title="Subject (whom the token refers to)" style="padding-right: 0.1px;">{</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" title="Subject (whom the token refers to)" style="padding-right: 0.1px;">\\"role\\":\\"data_user\\"</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" title="Subject (whom the token refers to)" style="padding-right: 0.1px;">}</span></pre>'; // Replaces inner HTML with JSON string
#     var parent = l2.parentNode;
#
#
#     while (l2.firstChild) {
#     l2.removeChild(l2.firstChild);
#     }
#
#     // Create a new pre element
#     var newPre = document.createElement('pre');
#     newPre.className = 'CodeMirror-line';
#     newPre.setAttribute('role', 'presentation');
#
#     // Create a span element
#     var newSpan = document.createElement('span');
#     newSpan.setAttribute('role', 'presentation');
#     newSpan.style.paddingRight = '0.1px';
#     newSpan.innerText = '{';
#
#     // Append the span to the pre element
#     newPre.appendChild(newSpan);
#
#     // Append the new pre element to l2
#     l2.appendChild(newPre);
#
#
#     // Create a new pre element
#     var newPre = document.createElement('pre');
#     newPre.className = 'CodeMirror-line';
#     newPre.setAttribute('role', 'presentation');
#
#     // Create a span element
#     var newSpan = document.createElement('span');
#     newSpan.setAttribute('role', 'presentation');
#     newSpan.style.paddingRight = '0.1px';
#     newSpan.innerText = '"role": "data_user"';
#
#     // Append the span to the pre element
#     newPre.appendChild(newSpan);
#
#     // Append the new pre element to l2
#     l2.appendChild(newPre);
#
#
#     // Create a new pre element
#     var newPre = document.createElement('pre');
#     newPre.className = 'CodeMirror-line';
#     newPre.setAttribute('role', 'presentation');
#
#     // Create a span element
#     var newSpan = document.createElement('span');
#     newSpan.setAttribute('role', 'presentation');
#     newSpan.style.paddingRight = '0.1px';
#     newSpan.innerText = '}';
#
#     // Append the span to the pre element
#     newPre.appendChild(newSpan);
#
#     // Append the new pre element to l2
#     l2.appendChild(newPre);
#
#     parent.style.display = 'none';
#     parent.offsetHeight; // This forces a reflow
#     parent.style.display = ''; // Restore display property
#
#     // l2.createElement('<pre class=" CodeMirror-line " role="presentation"><span role="presentation" title="Subject (whom the token refers to)" style="padding-right: 0.1px;">{</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" title="Subject (whom the token refers to)" style="padding-right: 0.1px;">\\"role\\":\\"data_user\\"</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" title="Subject (whom the token refers to)" style="padding-right: 0.1px;">}</span></pre>');
#     // var l2 = l.getElementsByClassName("CodeMirror-code")[0];
#     // l2.parentNode.removeChild(l2); // Commented out, as you may not need to remove the element
#     // l2.parentNode.innerHTML = '<pre class=" CodeMirror-line " role="presentation"><span role="presentation" title="Subject (whom the token refers to)" style="padding-right: 0.1px;">{</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" title="Subject (whom the token refers to)" style="padding-right: 0.1px;">\\"role\\":\\"data_user\\"</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" title="Subject (whom the token refers to)" style="padding-right: 0.1px;">}</span></pre>'; // Replaces inner HTML with JSON string
#
# """)

ground_water_xpath = """cm-jwt-header"""
token_header = driver.find_element(By.NAME, "secret")
token_header.clear()
token_header.send_keys("JvJ5XuVlhe9RdkXU7nzzmhIpraYXwyDf")
value = token_header.get_attribute("value")


#time.sleep(sleep_timeout)
payload_div = driver.find_element(By.CLASS_NAME, "js-payload")
payload_role_data = payload_div.find_element(By.CLASS_NAME, "CodeMirror-code")
code_mirror_text = payload_role_data.get_attribute("presentation")
new_text_content = '{ "role": "data_user" }'

#driver.execute_script("arguments[0].innerText = arguments[1];", payload_role_data, new_text_content)

print(f"The code line is {payload_role_data.text}")
time.sleep(sleep_timeout)

payload_encryption_line = driver.find_element(By.CLASS_NAME, "CodeMirror-code")
print(f"The payload data is {payload_encryption_line.text}")

with open("jwt_key.txt", "w", encoding="utf-8") as file:
    file.write(payload_encryption_line.text)

driver.quit()
print(f"The value is {value}")

