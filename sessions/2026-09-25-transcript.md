# Workshop 1 transcript: agentic AI, models that take actions

Graduate seminar, Institute of Data and Analytics (IDA), Culverhouse College of Business, September 25, 2026.

- [Video recording](https://alabama.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=8d3f444c-8b6a-490b-9738-b4d00129a3a7)
- [Slide deck](../slides/agentic-ai.html) ([PDF](../slides/agentic-ai.pdf))
- [Getting started on a Mac](../getting-started/mac.md) or [on Windows](../getting-started/windows.md)

This is an edited transcript of the live session. It removes filler, false starts, and speech-to-text errors (e.g., "Pixie" for Pixi, "Clod" for Claude, "Carpazi" for Karpathy), and it replaces names of colleagues and students with their roles. Where I misspoke on a fact, the text below gives the corrected version, and the [corrections](#corrections) section at the end lists each change against what the recording says. Timestamps refer to the video. The transcript ends with the audience question at 00:57:54 and one point from a conversation after the session. The rest of the recording after the group photo is informal conversation and is not transcribed.

## Contents

1. [Welcome and goals](#welcome-and-goals-000000)
2. [AI, machine learning, deep learning, and language models](#ai-machine-learning-deep-learning-and-language-models-000246)
3. [From chat assistants to agents](#from-chat-assistants-to-agents-000434)
4. [The model and the harness](#the-model-and-the-harness-000625)
5. [Tools, memory, skills, and context](#tools-memory-skills-and-context-001054)
6. [From prompt engineering to loops and goals](#from-prompt-engineering-to-loops-and-goals-001316)
7. [Rambling as a way to give context](#rambling-as-a-way-to-give-context-001757)
8. [How long agents can work](#how-long-agents-can-work-001946)
9. [The student offer](#the-student-offer-002222)
10. [Demo 1: Codex analyzes the customer data](#demo-1-codex-analyzes-the-customer-data-002317)
11. [Demo 2: Claude Code, voice, and a Codex reviewer](#demo-2-claude-code-voice-and-a-codex-reviewer-003619)
12. [The exercises in the repository](#the-exercises-in-the-repository-004520)
13. [You own the output](#you-own-the-output-005349)
14. [Remote control and closing](#remote-control-and-closing-005445)
15. [Questions](#questions-005754)
16. [After the session: sensitive data](#after-the-session-sensitive-data-010350)
17. [Corrections](#corrections)

## Welcome and goals (00:00:00)

Hello. If you do not know me, my name is Dr. Freeman. I am on the operations management faculty here, and I am also associate director of our Institute of Data and Analytics. Two of my IDA colleagues are here to help if I get off the rails today. I am recording this session because what I want today is not so much fingers on keyboards. I want to show you some things you may not be aware of about how far AI has progressed, focused on use cases that could help in the work you do. We have a mix of master's and PhD students in the room, and I am convinced the concepts I talk through today are useful to both groups.

I have put all the content on GitHub. If you do not know what GitHub is, that is fine, and I will show you how to download from it. The first half of this session is me talking through ideas and concepts. After that we are going to roll the dice on some live demos, which could always go sideways. Everything I show is in the repository, because I do not want you to just come in here and listen. It is imperative that you go play. You are in a very different place than I was at your stage. You are entering a workplace with different expectations, and one of those expectations is that you understand this technology and have some fluency and competency in it. The only way to get that is by using it. You have to bump into the walls to figure out what you need to learn.

(00:01:50) The graduate programs office will share the GitHub link, which has the slide deck, the video, and all the content. Over the summer I reached out to the graduate programs office because many students, and many other people, come to me with AI questions and ideas. I see a lot of patterns in those conversations, and it feels to me that people are missing some of the big picture. That is why I wanted to get this group together, and in particular to talk about agentic AI, a phrase many of you have probably heard.

A quick show of hands. How many of you use AI, maybe every day? I would put my hand up twice for that. How many of you would say you are comfortable using generative tools? A few of you. Some of you may not know the difference between those, and that is where I want to start.

## AI, machine learning, deep learning, and language models (00:02:46)

I often hear people talk about AI and LLMs as if they were the same thing. They say, "I'm chatting with AI." An LLM is a large language model. When you interact with ChatGPT or a Claude model, you are interacting with an LLM. Because we hear "AI" so much, people now treat AI and language models as synonyms. They are not.

AI is a field that has existed since the 1950s. The term was coined for a 1956 workshop at Dartmouth. AI covers programs that let computers do things we typically associate with human intelligence. That could be an if-else statement in a program that makes a decision. There is no learned model underneath it, but if it mimics human decision making, it can be thought of as an artificial intelligence system.

Machine learning is a more specific term under that umbrella. I have a lot of data, the machine finds patterns in that data, and it encodes those patterns in a model that it uses to make decisions. Under machine learning are neural networks and deep learning, which are a particular type of model that learns from data. Language models sit there. They are a subset of a subset of artificial intelligence.

I bring this up because, for those of you going into the job market and talking with employers, understanding these differences and being able to talk about them intelligently matters. Language models are the focus today, but they are one form of artificial intelligence, not the whole of it.

## From chat assistants to agents (00:04:34)

How many of you mostly use AI in the browser, maybe at chatgpt.com or claude.ai? That is fine. Your interaction probably looks like this. I have a chat assistant in the browser, I ask questions, it gives me answers, and maybe I copy and paste into a document. It is a back-and-forth chat.

(00:05:32) Today we are talking about agentic AI. Think about the word "agent". Where have you heard it before? A sports player has an agent, and someone in Hollywood books work through an agent. What is an agent in that context? Someone who can operate on my behalf. That is the key difference between traditional chat and agentic AI. In agentic AI, we place the model's intelligence inside a harness and give it access to tools and resources that let it take actions on our behalf. That is very powerful, and we are going to demo it.

## The model and the harness (00:06:25)

When we talk about language models today, we usually talk about the model. The model is an important piece of an agent-based system, but it is not the only important piece. I think analogies help here, so think about your computer. What would you call the brain of your computer? You would probably say the processor. An Apple M5 chip with 12 cores is more capable than the dual-core Pentium chip I grew up with. That is how I want you to think about the model.

(00:07:14) If you have a very good processor and nothing else, do you have a computer? You do not. You need to put that processor inside something, which in a computer is the operating system, i.e., Windows or macOS. The operating system gives the hardware pathways to interact with everything else on the machine. In an agent-based system, the harness is the wrapper around the model that gives it access to things called tools.

(00:08:08) Anything the harness exposes as a tool, the model can use to act on your behalf. It can read files, edit files, and search the web. There are also Model Context Protocol (MCP) servers, which connect the harness to additional tools. All of these are ways for the model to take actions.

A lot of context also flows into the harness. Besides containing the model, the harness provides guardrails, and those live in the context. Many of you know the term prompting. What you may not know is that when you use a harness, the provider injects a system prompt on your behalf. Anthropic has a system prompt that Claude Code adds, for example. The system prompt keeps the model within the boundaries the provider wants. If a person is talking about self-harm, the provider wants that conversation handled a certain way. You have heard about the cybersecurity and biological safeguards the labs have, and those rules are in the system prompt too. It gets sent along with your conversation.

(00:09:04) Back to the computer analogy. The processor is the brain, and the harness is the operating system that lets the model act. On your computer you also customize things. You have programs you like for word processing, and you might have TikTok installed (I pick on TikTok a lot). In the agentic world, tools connect the model to the outside world, and memory files and skills customize how the model behaves inside the harness.

(00:10:01) The key point is that the model is one piece. When I say "model", I mean something specific, such as GPT-6 Sol or Claude Opus 5.5. The harness is something like Claude Code or Codex, and I will show you what those look like. Additional files get read into the harness as well. The harness lets the model communicate with the outside world and take action, and it lets us inject our own preferences.

One more thing is emerging in how we interact with AI. In the browser, we ask questions back and forth. With agentic workflows we can still do that, but now the agent can act on our behalf. There is now a move toward a higher level of abstraction, where you act as a manager. You give the harness goals, and it orchestrates actions on your behalf in a loop, which lets it work autonomously on big, ambitious projects for a long time. We will demonstrate goals later.

## Tools, memory, skills, and context (00:10:54)

A quick pass through the parts. Tools are capabilities the harness provides that let the model take certain actions, such as running a command. Memory is usually files on your machine. If you run into a particular problem in a particular use case, you can tell the agent, "Let's remember this for the future." The next time you load the harness and work on something, you do not run into the same problem again. Skills are instructions the agent loads as needed for particular tasks. I will mention a skill I use for daily planning later.

(00:11:50) Another important idea is context. How many of you have heard the term? One answer from the room was that it is how much the AI can remember. That is close. Each model has a certain amount of context it can keep track of, measured in tokens. People often think a token is a word, but it can be a piece of a word. Different models have different context limits. Suppose I am working with a model that has a 200,000-token window, and I have a long conversation that reaches the end of it. Many harnesses can auto-compact, and you need to understand what happens when they do.

(00:12:20) When the harness runs out of context, it frees up space by summarizing. If you had an important detail in the first 50,000 tokens, and the window compacts, that detail might disappear without your knowing it. It is also not just your conversation that fills the window. The system prompt and every result that comes back from the tools the agent uses go into the window too. Long or cluttered context can also reduce accuracy before the window is full, which is called context rot. We will look at ways to manage it.

## From prompt engineering to loops and goals (00:13:16)

The situation you are in is hard, and I feel for you. Every week it feels like the world is moving underneath my feet. What happened this Tuesday? Some of my students know, because they have heard me talk about it. On Tuesday, September 22, the two major labs released three models. Anthropic released Claude Opus 5.5, which is a very good model. OpenAI released GPT-6 Sol and GPT-6 Luna about an hour later. There is talk that OpenAI may release another variant next week. The time between Opus releases keeps getting shorter. It is moving at a crazy pace, and you are going into a world where you are expected to stay on top of it. That is a challenge, and you need to figure out the right way to do it.

(00:14:16) Here are some terms you may have heard that we hear less often now. How many of you have heard of prompt engineering? We created special-topics classes on it. Does anyone know who this is? That is Boris Cherny, and he is not just any Anthropic employee. He created Claude Code. His quote is, "I don't write prompts for Claude anymore. I have a whole set of loops running. My job now is writing loops." According to the creator of Claude Code, he does not do prompt engineering anymore. That shows how fast things have changed. We started with prompt engineering. I will say that prompts still matter.

(00:15:15) Then we talked about context engineering. It is not just what we tell the model. It is what we tell the model plus everything else the harness gives it access to, such as memory files. Now we have moved to loop engineering, which is what Boris Cherny was describing. How can I give an orchestrator agent enough context that it can drive and prompt other agents itself? I tell it, "This is the vision. This is where I want to land. Work toward that, and tell me if you hit anything you cannot resolve on your own." Goals are the next step, i.e., loop engineering where the agent keeps working until a checkable condition is met. These two terms are at most six months old.

(00:16:11) People are already talking about the next term after these. I am not trying to scare you. I know AI is worrying for many people, and we are all in this together. I am not an AI doomer. I am an AI optimist, because I have seen the work it enables me to do. Projects that I used to put off for six months, I can now start with an agent. If one does not pan out, that is fine, because my time investment was so low.

(00:17:05) The idea behind loops and goals is that I, as the person with the overall vision for a project, give the agent a tremendous amount of context. The project could be a research project or a product goal for your company, which is why the same principles apply to master's and PhD students. Instead of saying, "Make this graph, do this analysis," one step at a time, I tell the agent what my vision is and why I have that vision. That gives it enough alignment to work toward the goal on its own.

## Rambling as a way to give context (00:17:57)

Has anyone heard of Andrej Karpathy? One student described him as someone who does some AI development. He does a little bit of AI. He was a PhD student of Fei-Fei Li at Stanford, who created the ImageNet dataset, and he worked on that project. He was the director of AI at Tesla, and he joined Anthropic in May of this year. He is a big deal.

(00:18:52) In July he posted about how he works with language models. Everybody had been asking how to do context engineering and how to think about prompts. His answer was that it matters less than people think. Turn on voice mode, do not worry about how you sound, and ramble to the model for about ten minutes. Whatever the project is, tell it your concerns, where you want to end up, and what you are uncertain about. Give it as much information as you can. With a loop set up around a goal, these models will figure out the rest. That is what we are going to demonstrate today, so you get to hear me ramble.

## How long agents can work (00:19:46)

If we give models the big picture and let them work in a loop, how long can they work? Has anyone seen this chart? It comes from METR, a nonprofit that evaluates frontier AI models. METR had human experts complete a suite of tasks and recorded how long each task took them, from seconds up to more than a day of work. For each model generation, the chart shows the length of human task the model can complete autonomously with a given success rate.

(00:20:35) Look at Claude Opus 4.6. At the 50% line, it succeeds half the time on tasks that take a human expert about 12 hours, i.e., more than a full workday, completed by an autonomous agent loop without asking for help. I know some people find that scary, but I see it as an opportunity. If you learn to work well with these systems, you can get that kind of productivity.

(00:21:29) This is the 50% curve. At the 80% success rate, the line shifts down, so the stricter horizons are several times shorter. The top point, Claude Mythos Preview, is past what METR's task suite can measure reliably, and the chart has no point yet for the models released this week. These models are amazing. If you have not played with them, you need to, and right now it is easy for you to do so.

## The student offer (00:22:22)

Many of you use ChatGPT or Claude, and I use both. OpenAI has an offer right now for students at U.S. colleges and universities. You can get four months of ChatGPT Plus, the $20 per month plan, for free. You have to claim it by October 31, and you need to verify enrollment and enter a payment method. The subscription renews at $20 per month afterward unless you cancel. Check the offer page for eligibility if you have had a subscription before.

A lot of people say they are not going to pay for AI. A paid plan gives you the full version of OpenAI's agentic tool, Codex, including the command-line version and the stronger GPT-6 Sol model. The free plan offers only limited Codex access. You need to play with it, so I encourage you to claim the offer.

## Demo 1: Codex analyzes the customer data (00:23:17)

I am going to show you some things, because once you see them, your brain cannot forget them. If you have only worked in the browser, you have not seen what these tools do. I will switch between Claude and Codex a little today. Please watch and ask questions.

For both Claude and OpenAI, there is a desktop app for Windows and Mac. This is OpenAI's app, which is now called the ChatGPT desktop app, and you choose Codex inside it. You may notice my operating system does not look like Windows. It looks like a Mac, but it is Linux.

(00:24:05) The Linux version of the app is not as good as the Windows or Mac versions, so I am going to use the terminal. Everything I do in the terminal, you can do in the app. Notice that in the app I can choose a location on my computer. Codex is the harness. It gives the model tools it can use on my computer, and instead of an interactive chat, it does agentic work on my behalf. The key point is that any tool installed on your machine that can be called from the terminal becomes available to Codex.

(00:25:04) Here is how to get the materials. On the GitHub repository page, click the green Code button and choose Download ZIP. The file lands in your Downloads folder. Right-click it and extract it. (I had already downloaded it once, so my computer asked about replacing files.)

(00:26:01) Now I have the folder. There are two examples in four folders. Two are about customer segmentation and two are about Reddit data. Both include datasets, because we are going to have the agent work with data on our behalf. The customer-segmentation folder is the completed version, with many files already built. The customer-segmentation-base folder has only a few files. The base folder is the "before" and the other is the "after". I have given you a transcript that you can hand to your agent, and it should produce something that looks like what is in the completed folder.

(00:26:58) I want to give the agent good tools, because with good tools it can do very good work. I am going to give it access to Python. You might say, "I don't know any Python." That is fine. Agents are very good at writing Python and many other languages.

I like a tool called Pixi, a package manager. On the Pixi website, the installation page shows how to install it on Linux, Mac, or Windows. Install it, and you are done.

(00:27:55) How do you know it worked? On a Mac, find the Terminal app, for example by searching for it with Spotlight. On Windows, open PowerShell. You might say, "Dr. Freeman, I don't know computers like that." My honest opinion is that learning your terminal is now part of the job. I am not asking you to be a computer scientist. I am asking you to learn to open a terminal and run a command, because avoiding it keeps you from the tools that will make you competitive. A short YouTube video will get you there. On Linux I click one button and the terminal opens. Type `pixi` and press Enter. If you see the help text, the tool is installed, and the agent can use it.

(00:28:52) Any questions so far? I have a copy of the repository on my desktop, with the customer-segmentation and customer-segmentation-base folders and the reddit and reddit-base folders. The Reddit data file is too big for GitHub. To get it, follow the link at the bottom of the README, which goes to Google Drive, download the file, and put it in the data folder.

(00:29:47) Let us work with the customer segmentation data. It is the Complete Journey dataset of supermarket transactions, which we used for an IDA case competition last year. The release in the repository is simulated and intended for education. For this demonstration I do not want the agent to have any additional context from the repository, so I copy the base folder to my desktop and remove everything except the data. All I have now are data files in a format I have never seen, Parquet.

(00:30:40) If I double-click one, my computer does not know what to do with it. Parquet is a binary format, and a very efficient one. Not knowing the format is not a limit, and I find that exciting. I want to be careful here. I am not saying you are not responsible for what these tools do. You still have to equip yourself to understand the results, check them, and ask questions. I will show you some practices that make agents less likely to go off the rails and make your work more reproducible. Overall, the models are very good.

(00:31:39) Let us run the first workflow. On Windows or Mac, you could open this folder in the desktop app and run it there. I am using the terminal. You would type `codex` (I use a custom alias on my machine, but you just need `codex`).

(00:32:34) Codex asks whether I trust this folder, and I do. This is the Codex harness running in the terminal. The model is GPT-6 Sol, one of the models released this week. Does anyone know what "medium" means here? Effort. These models can reason. Instead of answering immediately, the model generates thinking tokens that explore different paths before it answers. Effort controls how much of that thinking it does.

(00:33:29) To change the model or effort, type `/model` in the terminal, or click the model name in the desktop app. When I ask people what model they use, they often say "OpenAI". That is a provider, not a model. Which model do you use, and why do you prefer Sol over Luna? Understand the tradeoffs, because the models have different levels of intelligence and cost. I will use GPT-6 Sol at medium effort. Notice that I am in the customer-segmentation-base folder on my desktop.

(00:34:25) My prompt is, "I have a dataset of customer transactions in the data directory. Can you use Pixi to conduct an analysis of the purchasing trends and create an HTML report I can review?" I will not wait for it to finish. Because I told it to use Pixi, it will set up a Pixi environment in this folder, install packages, write the code, and run the code on my machine.

(00:35:24) Codex came back with two questions, which gives me a chance to steer. It asked where to create the project, and I said here. It also asked whether computed numbers should go into the HTML only. For the PhD students, a practice I use to keep analysis reproducible is to have the code write every reported number to a variables file that LaTeX imports. If the analysis changes, the document picks up the new numbers automatically, instead of the model retyping them.

(00:36:21) Now it is creating my environment and installing PyArrow and Matplotlib, and it is already running Python to get a sense of the data. This is agentic AI. I will let it keep working while I show you a different harness.

## Demo 2: Claude Code, voice, and a Codex reviewer (00:36:19)

Remember Karpathy's advice about rambling. Why does it matter that you can brain-dump to these tools? Think about typing a long prompt. A few prompts in, your hands get tired, you start getting lazy, and you stop communicating your real intent to the model. I can talk much faster than I can type, and I give the model far more context when I talk.

(00:37:49) You can do this in the Codex desktop app, which has a dictation button. That is the main reason I am not using the app today, since dictation does not work well in the Linux version. I will make another copy of the folder for Claude, so the two agents do not work in the same place.

(00:39:43) This is Claude Code, Anthropic's harness. If you have an Anthropic subscription, look up how to install Claude Code for your operating system. It has a desktop app too, but I use the terminal. It works the same way. I am in a folder, and I can choose my model. I am on Claude Opus 5.5, with a one-million-token context window.

(00:40:35) Here is something I like about Claude Code. Early on, people worried a lot about models hallucinating, and you still need to be careful. Anything AI produces on your behalf is still yours. You are the owner, so you have to be able to probe it and check it. Many people with one model ask an agent to create something and then ask the same agent to check it. That is biased, because the grader is the one who did the work.

(00:41:29) Claude Code has plugins, and one of them is a Codex plugin. If you have both tools, Claude can do the work and hand it to Codex with the instruction to prove it wrong. That works well. The key instruction is, "Do this analysis, and when you think it is done, hand it to Codex and tell it that its job is to prove you wrong. If it comes back with findings, verify them, and continue until you both agree."

(00:42:24) Claude Code also has voice mode in the terminal. I hold the space bar and talk. Here is what I said:

> I have a data folder in this directory, and I want you to conduct an exploratory analysis of the customer buying trends. In particular, I'm interested in whether we've seen upward or downward trends for certain categories of products. Come up with a way to conduct that analysis. If you have any questions, ask me. Generate some nice visualizations. An HTML report would be really nice. When you think you're done with the analysis, hand it over to a Codex subagent whose job is to find where you are wrong. I want them to evaluate your work and come up with a list of issues, and for each issue, tell you how they'd recommend fixing it. You verify all of those findings. Ask me if there's true ambiguity. If they offer a suggestion and you disagree, raise it with me, and I'll be the final decision maker. Otherwise, continue autonomously. When you're done with the HTML report, open it in a browser on my machine and look at it from the perspective of good user interface and user design. Make sure it clearly communicates the insights. Ask me any questions you have before you get started.

(00:44:21) That was much easier than typing it. Think back to Karpathy talking for ten minutes and how much vision you can put in. Tell the model where you are uncertain, where it might go off the rails, what your vision is, and why you want it. The more of that you give these models, the less you need to babysit them. You describe the paths, and they are smart enough to work through them.

## The exercises in the repository (00:45:20)

Now let me show you what is in the repository for you, because I want you to go home and play. You can get Codex free for four months. Install it for your operating system. I hate to sound this way, but "I'm not good at computers" is no longer a reason to skip this. AI is going to be expected in every industry, and whether you like it or not, the genie is out of the bottle. Our college has an AI advisory board with leaders from each of our disciplines. They told us that they are now looking for a three- to five-fold increase in productivity from entry-level hires.

(00:46:13) Where will that productivity come from? From understanding how to use agents correctly and how to manage them. That is the expectation, so start playing with them. Install Codex, and use the desktop app or the terminal, whichever you prefer.

(00:46:42) For each example there is a completed folder and a base folder: customer-segmentation and customer-segmentation-base, reddit and reddit-base. For the Reddit example, click the Google Drive link at the bottom of the repository's README and download the file, which is about 750 MB. It contains daily post counts for Reddit accounts, with consecutive daily coverage from January 2025 through September 2026 and sparser records before that. The accounts are integers, so nothing in the file points back to a username.

(00:47:33) You can use it to ask whether the number of posts on Reddit has changed, which we thought might be driven by bot activity.

(00:48:29) While that downloads, let us check on the agents. Codex has finished and created its HTML report. Claude is asking me questions. It asks what "trending up or down" should mean, and I answer share of total spend. It asks how to handle holiday weeks, which may be blips, and I tell it to fit the trend on all weeks and again with holiday weeks excluded.

(00:49:21) Once the Reddit file downloads, put it in the data folder of reddit-base, which is where the analysis expects it.

Here is what I did for you. For each dataset, I recorded a ten-minute ramble, Karpathy style, explaining the vision for a problem. One is aimed at research, for the PhD students. It asks whether we can build a statistically valid measure of change in potential bot activity on Reddit since agentic AI tools emerged. The customer segmentation one is more of a marketing problem.

(00:50:19) I have data on all these consumers, and I want a targeted marketing strategy for subsets of my customers. Help me understand the clusters of customers and what defines them, so I can decide how to segment them and what targeted strategy fits each segment. The agent does the cluster analysis and writes a report. The transcript file in each base folder is my raw recording. In addition to describing the problem, it sets up a loop. It tells the agent to conduct the analysis, make a plan, and send the plan to subagents for review. I did not set up a Claude-versus-Codex review, because I assume you only have Codex.

(00:51:15) At the end, I have the agent make a deliverable and set up a loop around it. I tell it to grade the deliverable on dimensions such as visual clarity and the correctness of what it displays. It sends the deliverable to a panel of three subagent reviewers, for example a marketing expert and a methods expert. In each round, each reviewer scores the deliverable on those dimensions. The main agent reads the scores and findings, verifies them, makes fixes, and hands the deliverable back to the reviewers. It keeps going until the score plateaus.

(00:52:09) That is how the loop works. The agents argue about the findings, and I have told them what success means to me. They keep pushing the scores on those dimensions as high as they can, and when they cannot improve further, they stop and present the result to me.

My machine has memory files and skills that yours will not have at first, so I made you an easier on-ramp. When you open Codex in a base folder, in the terminal or in the app, tell it to read SETUP.md.

(00:52:59) SETUP.md tells the agent to read the transcript, and it adds writing and review guidance that my own setup would otherwise supply. You can open the file and read it.

## You own the output (00:53:49)

Let us take a quick look at the agents. Codex finished and produced an HTML report after asking us two questions. Claude is still working. Remember that you own this. If you send it to your boss, it is your work, not the model's.

What is the next step? Look at the result and make sure you understand it. If you do not understand a trend, remember that the model still has the context. Have a conversation with it: "I don't understand what is going on in that month. Show me." Your job is not just "agent, go." Your job is to interpret the result, and the same is true for research. The agent can get you to a version one, or help you scratch an itch you have had. You no longer have to write all the Python yourself. Those of you who know me know I love writing Python, but it is freeing, because the bottleneck used to be my fingers and it no longer is.

## Remote control and closing (00:54:45)

One last thing, which you could see as good or bad. Claude Code has remote control. With it active, I can send this session a message from my phone. I just asked it to say hello to the class. If I have five machines running, which I do, I can drive all of them from anywhere. It usually waits until the current turn finishes before it answers. Codex has a similar feature.

(00:55:44) I am right at two o'clock. I know there is a lot more to cover, and the goal today was to throw some cold water on you and show you what these tools can do. If you want to go into more detail on the tools, I am happy to do another session. I cannot meet with each of you individually, because I do not have the time. If a group of you is interested, reach out to the graduate programs office and say you want to learn more. They will contact me, find a time, and we will find a room.

(00:56:37) You are in a position that I cannot fully understand, and I know there is a lot of uncertainty. It is our job to help you prepare, and my IDA colleagues feel the same way. If there are things we can do to help you build these skills, let us know, and we will try to make it happen.

## Questions (00:57:54)

**Student:** Do you think AI models will at some point be able to come up with new hypotheses? When I get results, I usually work in notebooks. How do we make sure the tools and methods an agent uses are correct?

**Dr. Freeman:** The first thing I would say is that you should not lose control of your code. If you prefer to look at it in notebooks, tell the agent that is your preference, and it will follow it. On my own projects, after I see an initial result, I go back and ask about specific results. I might say, "Make a marimo notebook that shows me exactly each of those components." It is not a one-way street. It is a conversation, and you are still in control as the orchestrator. If it does something you do not understand, ask it. That is your job.

(00:58:57) Do not just accept what it gave you. Many times I have done an analysis and not understood a method exactly. I ask the agent to pull that snippet into a notebook and walk me through it step by step, so that I can own it or ask further questions. Go play with it, and if we can help you learn to work with it better, let us know.

## After the session: sensitive data (01:03:50)

After the session, a student asked how to use agents with data that cannot be shared with a model provider. My answer, lightly edited, was this. For sensitive data, you do not have to put the data on the machine the agent works on. Tell the agent what the columns are and what their data types are, and have it build a synthetic dataset with the same structure. The agent builds and tests the analysis on the synthetic data. You then run that analysis on your real data yourself, without the model ever seeing it. Local models, which run entirely on your own hardware, will likely also become important for sensitive data in the future.

## Corrections

These are the places where the edited text differs in substance from what I said in the recording.

| Time | Said in the recording | Corrected text |
|---|---|---|
| 00:07:14 | An "N5" chip | An Apple M5 chip |
| 00:13:16 | "Opus five" came out on Tuesday | Anthropic released Claude Opus 5.5 on Tuesday, September 22, 2026, and OpenAI released GPT-6 Sol and GPT-6 Luna about an hour later |
| 00:10:01, 00:32:34 | "GPT-6 Soul" | GPT-6 Sol |
| 00:15:15 | Paraphrase of Boris Cherny, "Claude writes the prompt, and now I'm talking to the new Claude that is coordinating" | His quote, "I don't write prompts for Claude anymore. I have a whole set of loops running. My job now is writing loops." |
| 00:19:46 | METR is "a company that does benchmarks for the AI companies" | METR is a nonprofit that evaluates frontier AI models |
| 00:20:35 | Claude Opus 4.6 completes 50% of tasks that take eight hours | METR's estimate for Claude Opus 4.6 is about 12 hours at 50% success, as the deck shows |
| 00:21:29 | For Opus 5, "they stopped measuring" | The highest point on the chart, Claude Mythos Preview, is past what the task suite measures reliably, and the chart has no point yet for the models released that week |
| 00:22:22 | Codex is not available on the free plan, and the offer is "either Plus or Pro" | The offer is ChatGPT Plus. OpenAI's pricing page lists limited Codex access (GPT-6 Luna in the desktop app) on the Free and Go plans, while the Codex CLI and GPT-6 Sol require Plus or higher |
| 00:22:22 | Past subscribers still qualify for the offer | Eligibility terms are on the [offer page](https://help.openai.com/en/articles/20001493-chatgpt-back-to-school-offer-for-students), which should be checked directly |
| 00:26:58 | Agents are "actually written in Python" | The Codex CLI is written in Rust and Claude Code in TypeScript. The point was that models write Python well |
| 00:29:47 | The customer data were "pulled from a company that performs analytics for supermarket chains" | The Complete Journey release in the repository is simulated and intended for education |
| 00:46:42 | The Reddit file covers two years | The file has consecutive daily coverage from January 2025 through September 2026 and sparse records back to 2006 |
