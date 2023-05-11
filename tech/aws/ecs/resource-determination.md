# Gunicorn vs Celery in AWS ECS: Understanding Workers and Application Performance
Gunicorn and Celery are both integral tools for managing workload in web applications, and their applicability extends to AWS ECS (Elastic Container Service) tasks as well. The main difference lies in how these tools are configured and optimized in the context of AWS ECS. This document aims to demystify Gunicorn and Celery within an AWS ECS context and provide a decision tree to aid in the selection process.

Gunicorn in AWS ECS
Gunicorn, or 'Green Unicorn', is a Python WSGI (Web Server Gateway Interface) HTTP server. It is a pre-fork worker model, which means it forks off multiple worker processes to handle incoming requests.

Gunicorn is ideal for I/O-bound tasks, which are tasks that involve reading from or writing to external resources, like network connections or databases, and spend most of their time waiting for these resources.

In AWS ECS, you can run Gunicorn within Docker containers. The number of Gunicorn workers to run depends on several factors:

CPU Units: AWS ECS allows you to allocate CPU units to a task. As a rule of thumb, the number of Gunicorn workers should be (2 x $num_cores) + 1. In the context of ECS, it's better to use (1 x $num_cores) + 1 as the formula for the number of workers, because the 2x multiplier assumes that your CPU will be waiting on a lot of I/O, which might not be the case within AWS ECS.
Memory: Each worker uses some amount of memory, so be sure not to exceed your task's memory limit.
Celery in AWS ECS
Celery, on the other hand, is an asynchronous distributed task queue. It allows you to distribute work across threads or machines. Celery is most suited for CPU-bound tasks or tasks that require heavy computation.

In AWS ECS, Celery workers can be run within Docker containers as separate tasks, or in the same task as your application if your tasks are not memory-intensive. Key factors to consider when configuring Celery:

CPU-bound nature: If the tasks are CPU-bound, you might want to limit the number of concurrent tasks to the number of vCPUs available.
Memory usage: More workers and higher concurrency means higher memory usage. Ensure that the combined memory usage of all your Celery workers and other processes does not exceed your task's memory limit.
Decision Tree
Nature of the task: If your tasks are I/O-bound, consider using Gunicorn. If they're CPU-bound, Celery might be more suited.
Concurrency: If you need to handle multiple requests simultaneously, Gunicorn's worker model might be the better fit. For tasks that can be executed in parallel or distributed across machines, Celery is more appropriate.
Memory: Always take into account your task's memory limit before increasing the number of workers in either Gunicorn or Celery.
Combination of Gunicorn and Celery in AWS ECS
In some cases, both Gunicorn and Celery can be used together within AWS ECS. A typical use case would be a web application where Gunicorn handles incoming HTTP requests and Celery handles long-running tasks in the background.

This setup allows the application to respond quickly to user requests while performing complex computations or I/O operations concurrently. However, it's crucial to ensure that the combined memory usage of Gunicorn, Celery, and any other processes does not exceed your task's memory limit.

Note: Balancing the number of Gunicorn and Celery workers in AWS ECS is an art. It requires understanding of the system's workload, careful observation, and continuous adjustment

# What counts as I/O
Yes, database read/write operations are typically classified as I/O-bound tasks. This is because these operations involve reading from or writing to a database, which is an external resource. During this process, the application is often waiting for the database to respond, hence it is "bound" by the I/O operation.

Here's a simple way to understand this:

I/O-bound tasks: These tasks spend most of their time waiting for input/output operations (such as network communication, disk operations, or in this case, database operations) to complete. The speed of these tasks can be improved by performing more operations concurrently (for example, with more threads or processes), as this allows the application to handle other tasks while waiting for the I/O operations to complete.

CPU-bound tasks: These tasks spend most of their time doing computations and don't need to wait for I/O operations to complete. The speed of these tasks can be improved by using a faster CPU or optimizing the algorithm to reduce the number of computations.

In reality, many applications have a mix of I/O-bound and CPU-bound tasks. It's important to identify the nature of your tasks in order to optimize your application's performance effectively.

# Determine resource usage using AWS Cloudwatch
Yes, you can monitor the I/O operations of an Amazon ECS container using Amazon CloudWatch, which collects metrics about your AWS resources and applications.

Here are some steps to access the relevant metrics:

Open the CloudWatch console.
In the navigation pane, click on "Metrics."
Under the "AWS Namespaces" section, click on "ECS."
In the ECS Metrics section, you can find metrics like "CPUUtilization" and "MemoryUtilization" for services and tasks.
Unfortunately, as of my knowledge cutoff in September 2021, ECS does not directly provide a metric for I/O operations at the container level.

However, you can monitor I/O operations at the Amazon EBS (Elastic Block Store) level if your ECS tasks use EBS volumes. The relevant metrics are "VolumeReadOps" and "VolumeWriteOps," which measure the completed read and write operations to an EBS volume.

Additionally, if your ECS tasks are running on EC2 instances, you can use EC2 instance metrics to get some insight into the I/O operations. Relevant metrics include "DiskReadOps" and "DiskWriteOps."

Remember to consider the nature of your application when interpreting these metrics. High I/O could be normal for I/O-bound applications like web servers or databases.

For more detailed I/O tracking or for applications inside the container, you may need to install a monitoring agent that provides more granular insights, or consider using a profiling tool specific to your application or programming language.

# Factors in decision
In the context of your ECS container's operation, which involves looking up a database record and then sending an SMS message via Pinpoint or Twilio's API, there are several factors to consider when deciding the number of Gunicorn and Celery workers to configure:

1. Nature of the Tasks
Your tasks are predominantly I/O-bound, as they involve waiting for a database response and then waiting for the SMS service to handle the request. Gunicorn is often well-suited for handling such tasks because it can manage other requests during wait times. However, if these tasks are part of a longer, more complex task that can be efficiently distributed and performed in the background, you might want to use Celery.

2. Concurrency
If you need to handle multiple requests simultaneously, consider increasing the number of Gunicorn workers. This will allow your application to process other requests while waiting for the database or the SMS API to respond.

3. Workload
You should consider the expected workload of your application. If your ECS container needs to handle a high volume of requests or perform a large number of SMS operations in a short period of time, you may need more workers to handle the load.

4. Resource Limits
Consider the CPU and memory resources available to your ECS task. Each Gunicorn or Celery worker will consume some amount of CPU and memory. You'll need to ensure that the total resource usage of all your workers does not exceed your task's resource limits.

5. SMS API Rate Limits
APIs like Twilio or AWS Pinpoint often have rate limits, which limit the number of API calls you can make in a certain period of time. If your application makes API calls at a rate that exceeds these limits, the API calls will fail. You should ensure that the number of workers you configure does not cause your application to exceed these rate limits.

Conclusion
Balancing the number of Gunicorn and Celery workers is an art and requires careful observation and continuous adjustment based on the above factors. You might have to experiment with different configurations to find the optimal balance for your specific application.

# Determination Decision Tree
When designing a decision tree for configuring Celery and Gunicorn workers in your context, it's important to consider several factors. Here's a guideline:

1. Determine the Expected Load per Worker
First, calculate the expected load per worker. This will help you estimate the number of workers you need to handle 20 million requests a day.

On average, there are about 86,400 seconds in a day.
If you're handling 20 million requests per day, that's approximately 231 requests per second.
Each worker will handle a portion of these requests. The number of requests a worker can handle per second depends on the time it takes to process one request (database lookup and SMS sending). Measure this time under normal conditions to get an accurate estimate.

2. Estimate the Number of Celery Workers Needed
Since Celery is pulling tasks from the SQS queue, the number of Celery workers needed will depend on the rate at which tasks are added to the queue and the time it takes for a worker to process a task.

If tasks are being added to the queue faster than they're being processed, you might need more Celery workers.
If tasks are being processed faster than they're being added to the queue, you could potentially reduce the number of Celery workers.
Keep in mind that each Celery worker will consume some amount of CPU and memory, so ensure that the total resource usage of all your workers does not exceed your task's resource limits.

3. Estimate the Number of Gunicorn Workers Needed
Gunicorn is handling incoming HTTP requests to your ECS containers. The number of Gunicorn workers you need will depend on:

The number of concurrent requests your ECS containers need to handle.
The time it takes to process one request.
Again, remember that increasing the number of Gunicorn workers will increase the CPU and memory usage of your ECS containers.

4. Monitor and Adjust
After estimating the number of Celery and Gunicorn workers needed, monitor your system's performance and adjust the number of workers as needed. Key metrics to watch include:

Queue length: If the queue length is consistently high, you might need more Celery workers.
CPU and memory usage: If your ECS containers are consistently hitting their CPU or memory limits, you might need to reduce the number of workers or increase the resource limits.
Response times: If your ECS containers are slow to respond to requests, you might need more Gunicorn workers.
This decision tree provides a starting point for determining how many Celery and Gunicorn workers to configure. However, remember that tuning the number of workers is more of an art than a science, and it might require some experimentation and adjustment based on your specific needs and constraints.

# how does gunicorn work
Gunicorn, or "Green Unicorn", is a Python Web Server Gateway Interface (WSGI) HTTP server. It is a pre-fork worker model, which means that it forks multiple worker processes to handle incoming requests. This is in contrast to a threaded model where threads are used to handle requests.

Gunicorn acts as an intermediary between your web application and the internet. When a request comes in, Gunicorn selects a worker process to handle the request. The worker process runs your application code and sends the response back to Gunicorn, which then sends the response to the client.

Here's a simplified step-by-step breakdown of how Gunicorn works:

Master Process: When you start Gunicorn, it creates a master process. The master process is responsible for managing worker processes.

Worker Processes: The master process then forks several worker processes based on the configuration settings. Each worker process is a separate instance of your application, capable of handling one request at a time.

Request Handling: When a request comes in, it's handed off to one of the available worker processes. The worker process executes the application code and generates a response.

Response: The worker process sends the response back to the master process, which then forwards it to the client.

Worker Management: The master process monitors the worker processes and creates new ones or kills existing ones as necessary based on the configuration and the current load.

One of the key features of Gunicorn is its configuration options. You can adjust the number of worker processes, set the type of worker class (sync or async), configure logging, and more. These options allow you to tune Gunicorn's performance to match your application's needs and the available server resources.

Note that Gunicorn is not meant to face the internet directly in a production setting. It doesn't handle slow clients, which can tie up your server's resources, so it's typically placed behind a reverse proxy like Nginx or a load balancer that handles incoming client connections.

# how does celery work 
Celery is an asynchronous task queue/job queue system based on distributed message passing. It is focused on real-time processing, but also supports task scheduling.

Here's a simplified explanation of how Celery works:

Task Definition: Tasks are defined in your application code as functions, and decorated with the @app.task decorator to tell Celery they're tasks.

Task Queue: When you want to run a task, instead of calling the function directly, you call the .delay() or .apply_async() method on the task function. This adds the task to the task queue.

Broker: The task queue lives in a separate service called a message broker. The broker's job is to distribute tasks to workers. Celery supports several brokers like RabbitMQ, Redis, and others.

Workers: Workers are separate processes or machines running instances of your application that listen for tasks from the broker. When a worker receives a task, it executes it.

Result Backend: After a task is done, the result can be stored in a result backend. This is optional and not necessary for simply executing tasks, but it's useful if you need to keep track of task results or if your tasks are part of a chain or group of tasks. Like brokers, Celery supports several options for result backends, including relational databases and message brokers like RabbitMQ or Redis.

Concurrency: Each worker can also be configured to run multiple tasks concurrently, either by spawning multiple processes or using event-driven IO (with the help of libraries like gevent or eventlet). The optimal type and level of concurrency depend on the nature of the tasks and the kind of workload you're dealing with.

Celery's architecture allows it to scale easily; you can start additional workers on more machines as your task volume increases. It also supports prioritization, task retries, and task expiration, and it provides a robust set of tools for inspecting and debugging task execution.

# how do they work at the processor level
Celery and Gunicorn are both written in Python, and they both use processes and threads to handle parallel tasks. However, they use these resources differently, and they're generally used for different types of workloads.

Gunicorn:
Gunicorn, or Green Unicorn, is a Python WSGI HTTP server. It uses a pre-fork worker model, which means it creates a master process that forks off worker processes to handle individual requests.

Each worker process runs in its own space in memory, and each one is capable of running a single thread of execution. This means that each worker process can handle one request at a time.

When a request comes in, Gunicorn's master process assigns it to one of the worker processes. The worker process executes your application code, generates a response, and sends it back to the client. The master process doesn't do much work itself - it mostly manages the worker processes and listens for new requests.

At the processor level, each worker process runs independently, which means they can take advantage of multiple CPU cores. However, because they're separate processes, they don't share memory with each other or with the master process. This isolation is good for security and stability (a crash in one worker doesn't affect the others), but it means that worker processes can't directly communicate with each other or share data without using a shared resource like a database or a cache.

Celery:
Celery, on the other hand, is an asynchronous task queue/job queue. It is designed to distribute tasks across multiple worker nodes, which can run on different machines or processors.

When you enqueue a task in Celery, it sends the task to a message broker (like RabbitMQ or Redis), which stores the task until a worker is ready to process it. A Celery worker then picks up the task from the broker, executes it, and (optionally) stores the result


# how cleery & gunicorn work together
Celery and Gunicorn often work together in a web application, but they serve different purposes and work in different parts of your system.

Gunicorn is a WSGI HTTP server. It's the part of your system that communicates directly with the internet. When an HTTP request comes into your system, Gunicorn is what receives the request. It then hands off the request to your application code (a Python WSGI application) for processing.

Celery, on the other hand, is an asynchronous task queue. It's used for offloading potentially long-running or resource-intensive tasks that you don't want to handle within the context of an HTTP request.

Here's an example of how they might work together:

An HTTP request comes into your system. This could be a user clicking a button on a web page, for example.

Gunicorn receives the HTTP request and hands it off to your application code.

Your application code decides that it needs to perform a task that could take a long time to complete, like sending an email or generating a report. Instead of doing this work immediately and making the user wait for the HTTP response, it enqueues the task with Celery and immediately responds to the HTTP request.

A Celery worker, which could be running on a different machine, picks up the task from the queue and starts working on it.

When the task is complete, the Celery worker might update the database or cache with the result of the task, or it might send a notification to the user. This depends on the specifics of your application.

So, Gunicorn and Celery work together by allowing your application to handle HTTP requests quickly and offload potentially slow tasks to be processed in the background. This allows your application to remain responsive and scale to handle large numbers of requests.

# Settings
## Overview for killing workers
Timeouts: Gunicorn's main process keeps track of each worker and how long it's been since the worker last checked in. If a worker process is stuck in a long computation, or is deadlocked and not releasing the GIL (Global Interpreter Lock), it won't check in with the master process. If the worker doesn't check in within a certain amount of time (controlled by the timeout configuration option), the master process assumes it's unresponsive and sends it a SIGKILL signal to terminate it. Then it spawns a new worker process to replace it.

Worker TTL (Time-To-Live): Gunicorn also has a max_requests configuration option that specifies the maximum number of requests a worker will process before it's automatically restarted. This can help mitigate memory leaks or other resource issues that might accumulate over the life of a worker process.

Signals: The Gunicorn master process and the worker processes communicate with each other using UNIX signals. For example, when the master process wants to gracefully shut down a worker, it sends it a SIGTERM signal. If the worker doesn't shut down within a certain amount of time, it sends a SIGKILL to forcibly terminate it. The worker processes can also listen for certain signals, like SIGINT or SIGQUIT, which indicate they should shut down.
## timeout
The default timeout in Gunicorn, which is the amount of time a worker process has to complete its work, is 30 seconds. This means that if a worker process does not respond within 30 seconds, the master process will kill and restart it.
## TTL 
The Gunicorn server does have a configuration option called max_requests which can be used as a kind of "Time to Live" (TTL) for worker processes. However, by default, this option is not set, meaning that worker processes will continue handling requests indefinitely and won't automatically restart after a certain number of requests.

If you want to set a TTL for your worker processes, you can do so by setting the max_requests configuration option in your Gunicorn configuration file or command line arguments. The value of max_requests is the maximum number of requests a worker will process before it's automatically restarted. This can help mitigate resource leaks over the life of a worker.

For example, you might set max_requests = 1000 in your Gunicorn configuration file to have each worker process automatically restart after handling 1000 requests.

There is also a max_requests_jitter setting which adds variability to max_requests. This can be used to stagger the restarting of your workers and prevent all workers from restarting at the same time.

Remember, these settings are not true TTLs in the sense of a time duration, but they serve a similar purpose by limiting the lifespan of each worker process.
## Signals
 The Gunicorn master process and the worker processes communicate with each other using UNIX signals. For example, when the master process wants to gracefully shut down a worker, it sends it a SIGTERM signal. If the worker doesn't shut down within a certain amount of time, it sends a SIGKILL to forcibly terminate it. The worker processes can also listen for certain signals, like SIGINT or SIGQUIT, which indicate they should shut down.