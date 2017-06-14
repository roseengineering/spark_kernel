
## spark\_kernel

This is a no-frills jupyter kernel to run the spark scala shell.  It provides no support
for inline graphics or incremental output.  However it is quite good for learning,
notebooking as well as prototyping code for spark, if that is what you need.

As an aside, if you are getting out of memory errors with spark, you probably need to
explicitly increase spark's memory use.  Spark reserves by default a minimal amount 
of memory.  One way to tell spark to increase memory is to set the environment variable 
SPARK\_MEM to the size you want before launching jupyter.

For example to increase spark's memory allocation to 6 GB use:

```bash
export SPARK_MEM=6g
jupyter notebook
```

To install spark\_kernel, run in this directory the script install.sh.
The script requires pip and python3 and uses sudo.

Copyright 2017 roseengineering
