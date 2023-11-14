starter: https://stackblitz.com/edit/nuxt-starter-zfyjug?file=server%2Fapi%2Floadzoo.js

outline:

http requests are a thing. computers send plain text back and forth. the text is simple but fulfills complex purposes. information gets requested and received. data gets got via get requests and sent via post requests. anthropomorphize requests. even when you're developing, this kind of request technically gets sent from your computer to your computer, we'll see

there are a few standard strategies for responding to requests: use the path to find a file (for example, an html file), use the path to look up some information in a database, use the path to locate a template and then fill that out... the current trend is to use a hybrid approach, where a template gets filled out with some html on the server and that gets sent to the web browser, and then the stuff in the web browser gets incrementally updated.

the zoo is sad. there's just one animal and it's the same for everyone.

this is how you create a login form with inputs and a button. the button will call this function when it's clicked. this function will send a post request with some data to the server.

now we have to create the response. to do that, we need to talk about javascript objects and data. javascript objects basically let you group variables together. the benefit, besides better organization, is that you don't have to know in advance what variable you're going to use by name; you can instead store a name in a string in a variable and change it over time. in other words, which variable you access doesn't have to be baked into the code; you can change it based on user input. you can have multiple groups, each with their own instance of the same variable. therefore, you don't even have to know what group of variables you're going to use; you can put these grouped-together usernames and passwords in an array and when you want to find the password corresponding to a username, you find the group of variables corresponding to that username and get the password from that. so you can put objects in arrays. you can also put arrays in objects. fun.
