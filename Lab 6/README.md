TEST
# m[Q](https://en.wikipedia.org/wiki/QAnon)tt[Anon](https://en.wikipedia.org/wiki/QAnon): Where We Go One, We Go All

## Prep

1. Pull the new changes
2. Install [MQTT Explorer](http://mqtt-explorer.com/)
3. Readings 
   * [MQTT](#MQTT)
   * [The Presence Table](https://dl.acm.org/doi/10.1145/1935701.1935800) and [video](https://vimeo.com/15932020)


## Introduction

The point of this lab is to introduce you to distributed interaction. We've included a some Natural Language Processing (NLP) and Generation (NLG) but those are not really the emphasis. Feel free to dig into the examples and play around the code which you can integrate into your projects. However we want to emphasize the grading will focus on your ability to develop interesting uses for messaging across distributed devices. 

## MQTT

MQTT is a lightweight messaging portal invented in 1999 for low bandwidth networks. It was later adopted as a defacto standard for a variety of Internet of Things (IoT) devices. 

### The Bits

* **Broker** - The central server node that receives all messages and sends them out to the interested clients. Our broker is hosted on the far lab server (Thanks David!) at `farlab.infosci.cornell.edu/8883`
* **Client** - A device that subscribes or publishes information on the network
* **Topic** - The location data gets published to. These are hierarchical with subtopics. If you were making a network of IoT smart bulbs this might look like `home/livingroom/sidelamp/light_status` and `home/livingroom/sidelamp/voltage`. Subscribing to `home/livingroom/sidelamp/#` would give you message updates to both the light_status and the voltage. Because we use this broker for a variety of projects you have access to read, write and create subtopics of `IDD`. This means `IDD/ilan/is/a/goof` is a valid topic you can send data messages to.
*  **Subscribe** - This is a way of telling the client to pay attention to messages the broker sends out on that topic. You can subscribe to a specific topic or subtopics. You can also unsubscribe
* **Publish** - This is a way of sending messages to a topic. You can publish to topics you don't subscribe to. Just remember on our broker you are limited to subtopics of `IDD`

Setting up a broker isn't much work but for the purposes of this class you should all use the broker we've set up for you. 

### Useful Tooling

Debugging and visualizing what's happening on your MQTT broker can be helpful. We like [MQTT Explorer](http://mqtt-explorer.com/). You can connect by putting in the settings from the image below.



![input settings](https://github.com/FAR-Lab/Interactive-Lab-Hub/blob/Spring2021/Lab%206/imgs/mqtt_explorer.png?raw=true)



Once connected you should be able to see all the messaged on the IDD topic. From the interface you can send and plot messages as well.



## Send and Receive 

[sender.py](./sender.py) and and [reader.py](./reader.py) show you the basics of using the mqtt in python.  Lets spend a few minutes running these and seeing how messages are transferred and show up. 



To run these examples make sure to install the packages from `requirements.txt`


## The One True ColorNet

It is with great fortitude and resilience that we shall worship at the altar of the *OneColor*. Through unity of the collective RGB we too can find unity in our heart, minds and souls. With the help of machines can  overthrow the bourgeoisie, get on the same wavelength (this was also a color pun) and establish [Fully Automated Luxury Communism](https://en.wikipedia.org/wiki/Fully_Automated_Luxury_Communism).



The first step on the path to *collective* enlightenment, plug in the [APDS-9960 Proximity, Light, RGB, and Gesture Sensor](https://www.adafruit.com/product/3595).

<img src="https://cdn-shop.adafruit.com/970x728/3595-03.jpg" height="300">

You are almost there!

The second step to achieving our great enlightenment is to run `python color.py`

You will find the two squares on the display. Half is showing an approximation of the output from the color sensor. The other half is up to the collective. Press the top button to share your color with the class. Your color is now our color, our color is now your color. We are one. 

I was not super careful with handling the loop so you may need to press more than once if the timing isn't quite right. Also I have't load tested it so things might just immediately break when every pushes the button at once.

You may ask "but what if I missed class?"

Am I not admitted into the collective enlightenment of the *OneColor*?

Of course not! You can got to [https://one-true-colornet.glitch.me/](https://one-true-colornet.glitch.me/) and become one with the ColorNet on the inter-webs.

Glitch is a great tool for prototyping sites, interfaces and web-apps that's worth taking some time to get familiar with if you have a chance. Its not super pertinent for the class but good to know either way. 



## Make it your own

Find at least one class (more are okay) partner, and design a distributed application together. 

I worked with Niki and Rob, who were instrumental in developing the code and final product. We also split the write up. We also got help from Ilan and David.

Rob's Code: https://github.com/rgentul/Interactive-Lab-Hub/blob/Spring2021/Lab%206/oven_set.py
Niki's Code: https://github.com/nagrawal44/Interactive-Lab-Hub/blob/master/Lab%206/distributed_banana_sender_joystick.py

**1. Explain your design** For example, if you made a remote controlled banana piano, explain why anyone would want such a thing.

We chose to design a distributed system for baking a cake (because you can't go wrong with cake). Each of our group members was in charge of a different piece of the cake-making system - cracking eggs, mixing ingredients, and baking the cake. We chose to represent these steps using different components of the pi.

While our design is more of an extreme example, this distributed system could be applied to large line kitchens where chefs need to communicate with each other without actually interacting. Mass production lines in particular would benefit from these systems.

**2. Diagram the architecture of the system.** Be clear to document where input, output and computation occur, and label all parts and connections. For example, where is the banana, who is the banana player, where does the sound get played, and who is listening to the banana music?

Each person does their respective job in the baking process, and then that input is transferred over MQTT to a centralized screen, which shows the next person that the step has been completed and that it is their turn to complete their part. Therefore they don't need to communicate or all be in the same place to know when to resume their part of the baking.

<img src="https://github.com/rkleinro-CT/Interactive-Lab-Hub/blob/Spring2021/Lab%206/imgs/Cake%20Diagram.jpg">

**3. Build a working prototype of the system.** Do think about the user interface: if someone encountered these bananas, would they know how to interact with them? Should they know what to expect?

We used tools that simulate what you would be doing when baking. The egg is cracked using a button, the batter is mixed using the joystick, and the oven is turned on using the twist stick, to simulate an oven dial. Therefore I think most people would know how to interact with it. The directions tell you whose step is up.

**4. Document the working prototype in use.** It may be helpful to record a Zoom session where you should the input in one location clearly causing response in another location.

https://iddlab6-mbas.glitch.me

https://cornell.zoom.us/rec/share/aCI2nLI-J_6404ME5aPzNJV3_117DD6lgdAnxoroOQ8zO75XBEBF5I02L7BHXQK_.MdkeZ86xKVyBp75q

**5. BONUS (Wendy didn't approve this so you should probably ignore it)** get the whole class to run your code and make your distributed system BIGGER.
