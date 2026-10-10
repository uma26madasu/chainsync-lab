When do I use a list, a dict, a set or a tuple?
What’s the difference between def and class?
What does try / except do, and why does ChainSync need it?
Why is incident["facility"] faster than searching a list for “facility”?list : ordered collection which can be changed, 

1. List, dict, set, tuple: half right. You said what each one is. The question asks when you’d use it. Add a real example to each:

List: things in order, like today’s alerts as they came in.
Dict: look something up by a name, like one incident’s details by field.
Set: remove duplicates, like which kinds of alerts happened.
Tuple: something that should never change, like a facility’s map location.

2. def vs class: close. “Totally a new thing” is too vague to say in an interview. Say it this way: def is a verb, a machine that does work. class is a noun, a blueprint for a new kind of thing.

3. try / except: correct. That’s a good ChainSync answer. One failed sensor or API shouldn’t stop the rest.

4. Why incident["facility"] is fast: wrong. incident is a dict, not a list. The real reason:

A dict jumps straight to the label, like opening a cupboard drawer marked “facility.” It takes one step, however many drawers there are.
A list has to check items one by one until it finds the match. With 10 items that’s fine. With a million alerts it’s slow.

 dict: info stored under keys, 
 set: collection of unique items,
tuple:order collection which cannot be changed. 
def:makes machine to do something,
class: totally a new thing,
try: go for attempt,except: if something goes off - record it, make a note , proceed  to next one. as for chainsync we do have many points or sensors and apis that are connected , if one is failed we dont want total process to be stopped.
incident["facility"] - reason is directly using LIST and picking the facility where incident happend, rather than using the searching all the facilities.

