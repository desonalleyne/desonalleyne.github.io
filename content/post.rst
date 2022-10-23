Page title
##########

:date: 2020-01-31
:tags: bash, terminal, commands,
:category: linux
:slug: 15_commands_every_linux_programmer_should_know
:author: Deson Alleyne
:summary: A list of linux commands
:title: Linux commands every Linux programmers should know
:lang: en
:status: published

Introduction
============

This is just an introduction

.. image:: /images/dima-pechurin-720X0NsgvfI-unsplash.jpg
    :alt: alternateText
    :width: 100%



.. raw:: html

   <span>Photo by <a href="https://unsplash.com/@pechka?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Dima Pechurin</a> on <a href="/?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText">Unsplash</a></span>


1.  man / help
==============

The **man** (manual) and **help** commands are probably the first two commands any Linux developer should know. The **man** command provides description and usage details of virtually any command/application you can execute in the terminal. The help command is similar but provides a more concise information on the command. These two commands are called in slightly different ways. 

The **man**, preceeds the command or application you're looking up::

   man <command>


The **--help** follows the command you'd like help on::

   <command> --help
    
Usage
**man**:

.. code-block:: bash

   $ man ls

You can navigate the manual using ``j`` (scroll down) and ``k`` (scroll up) or ``d`` and ``u`` for scrolling half page downward and upward respectively. To quit the manual, use ``q``.


**help** on the ``ls`` command:

.. code-block:: bash

   $ ls --help

This gives a brief (but often sufficient) indication of the arguments a command allow. 

   
2. ls
=====

Unless you've got really good photographic memory and remember where every file and folder is, you'll need the **ls** command. This command lists information about files and directories and makes working in a non-GUI environment possible. To see possible arguments for this command, you can combine it with the help or man  commands from above.

To demonstrate the usefulness of this command, I'll perform it in my ``demo`` directory. 

Here's the ``demo`` folder structure::
   
   ../demo/
   ├── days.txt
   └── names.txt

   
   
Usage

.. code-block:: bash

   $ ls 
   days.txt  names.txt

This command has a host of possible arguments you can specify to determine how the results are displayed.

My favourite arguments are: 

.. code-block:: bash

    $ ls -lrth
    total 8.0K
    -rw-r--r-- 1 pi pi 176 Feb 26 19:27 names.txt
    -rw-r--r-- 1 pi pi  57 Feb 26 19:52 days.txt
    
(Try using **--help** on the **ls** command to see available arguments)


3. grep
=======

This is probably one of most commonly used commands. Simply put, **grep** allows you to search. The cool thing is flexibility that the command provides via its arguments and options, and the fact that the search can be applied to virtually anything in the terminal.

Lets say you wanted to search for all lines in a file containing the word 'Guyana'.

You can achieve this by 'grepping' the file for the pattern 'Guyana'.

.. code-block:: bash

	# names.txt
        Name,Country
        Brian Lara,Trinidad & Tobago
        Shivnarine Chanderpaul,Guyana
        Ramnaresh Sarwan,Guyana
        Chris Gayle,Jamaica
        Darren Bravo,Trinidad & Tobago
        Christopher Barnwell,Guyana

Usage:

.. code-block:: bash

	$ grep Guyana name.txt
        Shivnarine Chanderpaul,Guyana                 
        Ramnaresh Sarwan,Guyana                       
        Christopher Barnwell,Guyana                   

Note that this command doesn't just apply to files. [[ADD MORE WAYS HERE]]



4. less
=======

This command allows us to view contents of a file, or output from a command in a pager (a scrollable view). It is very useful for reading files with hundreds of lines (eg log file for an application) and even has built-in searching capability.
The examples below demonstrate how to view contents of a file, and output of another command with the less command. Note: press the 'q' key to quit the pager and return to the terminal.

.. code-block:: bash

    # names.txt
    Name,Country
    Brian Lara,Trinidad & Tobago
    Shivnarine Chanderpaul,Guyana
    Ramnaresh Sarwan,Guyana
    Chris Gayle,Jamaica
    Darren Bravo,Trinidad & Tobago
    Christopher Barnwell,Guyana

Usage

.. code-block:: bash
   
   $ less names.txt
   Name,Country
   Brian Lara,Trinidad & Tobago
   Shivnarine Chanderpaul,Guyana
   Ramnaresh Sarwan,Guyana
   Chris Gayle,Jamaica
   Darren Bravo,Trinidad & Tobago
   Christopher Barnwell,Guyana
   names.txt (END)                          




grep with less

.. code-block:: bash

   grep Guyana names | less


5. cat
======

The cat command conCATenates files together and prints the results to standard output (your screen). In other words, if you needed to merge the contents of files, the cat command can do this. Since this command prints the content to standard output, I often use it when I quickly need to see what's in a file or to join files.


.. code-block:: bash

    # girls.txt
    Jane
    Mary

    # boys.txt
    John
    Mark


Usage

.. code-block:: bash
   
   $ cat girls.txt boys.txt
    Jane
    Mary
    John
    Mark


Bonus tip: you can write the resulting output of this command to a file using the redirect command **>**. This redirects the output from our cat command into a file, allnames.txt.

.. code-block:: bash
   
   $ cat girls.txt boys.txt > allnames.txt

6. cut
======

This command does exactly it sounds like. It cuts the specified segment of each line in the file. Segments can be specified positionally i.e. from 5th character to 10 character, or by delimiters (a specified character). As with all the other commands, the --help flag and the manual are your friends. 

Usage: 
If you want to segment the file by a delimiter, use the -d flag and specify the delimiter. You'll also need to specify which fields should be returned using the -f argument and the segment(s) you want returnede.

.. code-block:: bash

   # names.txt
   Name,Country
   Brian Lara,Trinidad & Tobago
   Shivnarine Chanderpaul,Guyana
   Ramnaresh Sarwan,Guyana
   Chris Gayle,Jamaica
   Darren Bravo,Trinidad & Tobago
   Christopher Barnwell,Guyana
 
To split the file into segments delimited by a , (comma) and return the 2nd field (countries), we can do the following:

.. code-block:: bash

   $ cut -d ',' -f 2 names.txt
   Country
   Trinidad & Tobago
   Guyana
   Guyana
   Jamaica
   Trinidad & Tobago
   Guyana


To split the file based on number of characters, we can use the -c argument and specify the position of the character(s) we want returned:

.. code-block:: bash

   $ cut -c 1-5 names.txt	
   Name,
   Brian
   Shivn
   Ramna
   Chris
   Darre
   Chris


What commands would you use to get the first name of each cricketer?

7. head and tail
================

No, we're not flipping a coin here. These two commands print content at the the top (head) or bottom (tail) of a file to screen. They come in very handy when I need to peek at a few lines in a file. By default they both show 10 lines, but you can change this behaviour using the arguments available.


.. code-block:: bash

   # names.txt
   Name,Country
   Brian Lara,Trinidad & Tobago
   Shivnarine Chanderpaul,Guyana
   Ramnaresh Sarwan,Guyana
   Chris Gayle,Jamaica
   Darren Bravo,Trinidad & Tobago
   Christopher Barnwell,Guyana

If we wanted the first 3 lines in a file, we can do:

.. code-block:: bash

   $ head -n 3 names.txt
   Name,Country
   Brian Lara,Trinidad & Tobago
   Shivnarine Chanderpaul,Guyana

Conversely, if we wanted the last 2 lines we can do:

.. code-block:: bash

   $ tail -n 2 names.txt
   Darren Bravo,Trinidad & Tobago
   Christopher Barnwell,Guyana

8. alias
========

The alias command makes you do magic with less keystrokes! This command essentially allows you define a shortcut/a literal alias for any command/s. Think of it as a tinyurl for commands. Lets say your terminal had a magical command named thisisanimaginarycommandthatdoesmagic. Typing this command every time would eventually get boring and possibly annoying. Also, that's about 100 keystrokes. To spice up your terminal, you can create an alias for this command and call the alias in the terminal instead.

Note: aliases created in this manner are temporary and only exist for this terminal session. 
I'll share steps on making these permanent in another post.
	
Usage

.. code-block:: bash

   # Creating an alias to echo a sentence to the screen
   # Note NO spaces between the = (equal) sign
   $ alias doMagic='echo "This Is An Imaginary Command That Does Magic"'

.. code-block:: bash

   # using an alias
   $ doMagic
   This Is An Imaginary Command That Does Magic

Whenever I call the `doMagic` alias, whatever is on the right hand side of the = (equal) sign is executed. In this case, it echoes "This Is An Imaginary Command That Does Magic" to the screen.

It might seem trivial but if used smartly, this command **WILL** save you tons of time and keystrokes!

Here's one of my favourites regarding the `ls` command. Try it out to see what it does:

.. code-block:: bash

   # set ls command to display more details
   $ alias ls='ls -lrth'



9. history
==========

The history command displays a history of all the commands you've entered in the terminal.
This command is especially useful when you're too lazy to retype a command you used in the past, or you want to see the timestamp you executed a particular command. 

By default, timestamp is not included in the results. Add the following line to your ~/.bashrc file to enable timestamps in the history command. You can add as many aliases to your ~/.bashrc file but you'll need to source it for any changes to apply.

.. code-block:: bash

   export HISTTIMEFORMAT="%F %T"

Then execute the following in your terminal to apply the changes:

.. code-block:: bash

   source ~/.bashrc


Usage:

.. code-block:: bash

   # Here are the most recent commands I executed in my terminal
   $ history
   ...
   601  2019-12-27 21:13:54 ls -lrth
   602  2019-12-27 21:13:58 cd
   603  2019-12-27 21:13:59 pwd
   604  2019-12-27 21:14:01 ls 
   605  2019-12-27 21:14:03 history
   606  2019-12-27 21:14:14 fg


10. wc
======

This command counts characters, words, and lines in a file. This might come in handy if you're typing your 5000 word essay in the terminal and wondering if you hit the target.

.. code-block:: bash

   # names.txt
   Name,Country
   Brian Lara,Trinidad & Tobago
   Shivnarine Chanderpaul,Guyana
   Ramnaresh Sarwan,Guyana
   Chris Gayle,Jamaica
   Darren Bravo,Trinidad & Tobago
   Christopher Barnwell,Guyana


Usage:

.. code-block:: bash

   # count number of lines in names.csv
   $ wc -l names.csv
   7 names.txt

   # count number of characters in names.csv
   $ wc -c names.csv
   176 names.txt

11. htop
========


If you're coming from a Windows background, you might be familiar with Windows Task Manager. I think of htop as the equivalent in Linux. This command launches an interactive process monitor that shows running processes and resource usage, and allows you to manage these processes. 
 
12. pipe character |
====================

The pipe character allows you to redirect output from one programm/command as input to another programm/command. 

(usually on the same key as the \ character). This will give you the ability to 'chain' multiple commands. eg: grep + wc...search for a particular pattern then count the number of lines that matched.

Here is an example of the pipe character in action:

.. code-block:: bash

   # names.txt
   Name,Country
   Brian Lara,Trinidad & Tobago
   Shivnarine Chanderpaul,Guyana
   Ramnaresh Sarwan,Guyana
   Chris Gayle,Jamaica
   Darren Bravo,Trinidad & Tobago
   Christopher Barnwell,Guyana

Usage:

.. code-block:: bash

   # search for Guyana in names.txt and pipe output to wc
   $ grep Guyana names.txt | wc -l
   3

13. bg, fg, jobs
================

These commands give you the ability to put processes (aka jobs) in the background (bg) or foreground (fg).
Lets say you executed 

   less names.txt

but now you need to take a quick look at another file. You can move the `less` process to the background using the key combination **Ctrl + z**

After hitting the key combination you should see 

.. code-block:: bash

   $ less names.txt
   # Ctrl + z pressed
   [1]+  Stopped                 less names.txt


The number in square brackets [1] identifies the job id. You'll need this if you want to bring the job back to the foreground

.. code-block:: bash

   $ fg 1

This will bring the job with id **1** to the foreground.

You can use the jobs command to see a list of jobs and their statuses.

.. code-block:: bash

   $ jobs
   [1]-  Stopped                 less names.txt
   [2]+  Stopped                 less days.txt


Summary
=======

This is just a brief (unexhausted) list of commands 
