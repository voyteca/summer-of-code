There is a lot of food to prepare and cook for the barbeque. You need to make sure you have enough time to do all the work before the guests arrive.

The tasks to be performed are listed in 04-preparation.txt. There's one task per line. Each line starts with the one-word name for that task, followed by the time that task takes, and finally the names of all the tasks it depends on.

For instance, here's a summary of eight tasks you have to do:

quesadilla 18
asparagus 12 tuna barley
barley 20
linguine 20 quesadilla barley
parsnip 20
kingfish 17 barley linguine porter
porter 12 quesadilla barley
tuna 20 porter
There's no particular order in the file: tasks can be listed in any order, and the dependencies can be listed in any order on each line. There are no cycles in the dependencies: no task depends on a task which depends on it (directly or indirectly).

The example shows that the task quesadilla takes 18 minutes and barley takes 20 minutes. All told, these tasks will take you 139 minutes to complete them all.

Part 1
Given the instructions file in 04-preparation.txt, how long will it take you to complete all the tasks?


You've realised that sorting everything out on your own is impractical, and you need help to get things finished on time. The good news is that you've recruited a lot of friends to help you; so many, in fact, that your pool of helpers is effectively unlimited. This means that you can have several tasks being worked on at the same time.

In the example above, the tasks quesadilla and parsnip can be done straight away, but you can't start tuna until porter has been done, and you can't start porter until both quesadilla and barley have been completed. kingfish requires three tasks to be finished before you can start it.

You can draw up the dependency network between the tasks, and it will look something like this:
![alt text](https://github.com/voyteca/summer-of-code/2018/Task4-Food_factory/task4-sample.png)


A network of tasks and dependencies

In this case, three people can start work on quesadilla, parsnip and barley at the same time. After 18 minutes, quesadilla is finished and someone can start work on linguine. After 20 minutes, barley is done and someone else can start work on porter. After 38 minutes, kingfish can start. It will take 64 minutes for you and your friends to complete the lot. 

Part 2
The instructions are still in 04-preparation.txt. With unlimited help, how long will it take to complete all the tasks?
