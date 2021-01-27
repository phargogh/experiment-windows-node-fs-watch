# Objective:

Figure out when node's `fs.watch` reports back about a file change.

# To Run

1. In a new shell, run `python generate.py` to start 1s generation to a new
   file.  Use append or write mode (comment out appropriate line in
   `generate.py`) as needed.
2. Run `node .` to run the node monitoring program.

# Conclusion

`fs.watch` will only call back the listener when the file is closed.

When the file is deleted, we have a rename event, not a change event.

When python's FileHandler opens a file, it keeps the file handle around until
the file is closed.  Therefore, the file will only appear in the output of
node's `tail` module when the model finishes running.

There are two possible workarounds for this:

* Use `fs.watchFile`, which will poll the modification times of the file in
  question.  Tail uses this information to keep polling new parts of the file.
* Write our own python FileHandler which will close and re-open the logfile
  on some interval, which will trigger Windows to pick up the file updates.

