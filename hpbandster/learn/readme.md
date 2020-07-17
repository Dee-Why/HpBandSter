# readme
I create this folder to write the thing I learned to understand this repository

I focus on HpBandSter/hpbandster/core/  and HpBandSter/hobandster/examples

to understand the code, I first learned the `multiprocess` module (which usually imported as `multiprocessing`)

then I read the first four examples in the ../examples/ folder and read related part in the ../core/ folder

## 一些看起来很重要但我还没完全理解的内容

### 关于contex

Alternatively, you can use [`get_context()`](https://docs.python.org/3.5/library/multiprocessing.html#multiprocessing.get_context) to obtain a context object. Context objects have the same API as the multiprocessing module, and allow one to use multiple start methods in the same program.

```
import multiprocessing as mp

def foo(q):
    q.put('hello')

if __name__ == '__main__':
    ctx = mp.get_context('spawn')
    q = ctx.Queue()
    p = ctx.Process(target=foo, args=(q,))
    p.start()
    print(q.get())
    p.join()
```

Note that objects related to one context may not be compatible with processes for a different context. In particular, locks created using the *fork* context cannot be passed to a processes started using the *spawn* or *forkserver* start methods.

A library which wants to use a particular start method should probably use [`get_context()`](https://docs.python.org/3.5/library/multiprocessing.html#multiprocessing.get_context) to avoid interfering with the choice of the library user.



