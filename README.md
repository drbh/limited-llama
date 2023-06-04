## What were doing here

This is a smol research effort into metaprogramming large language models.

Since LLM's produce output in a token by token fashion, we can use a context free grammar to constrain the output of the model. Going a step further we can define grammers that are progressively constrained based on ealier tokens.

The goal of this work is to explore how we can embed logic during generation to produce more coherent and consistent results. Most existing work in this area has focused on post processing the output or input of the model. We are interested in exploring how we can embed this logic into the model itself, and how to effectively and efficiently design a grammar or language that can express these ideas.

Testing constrained llm responses
```bash
# terminal 1
./limited \
    --seed 1 \
    -m models/openllama/ggml-openllama-3b-350bt-q4_0.bin \
    --grammar ../grammar/compiled_grammar \
    -f ../prompts/propose.txt

# terminal 2
python3 scripts/listener.py
```



### How we got here

For reference, the patch was created with the following commands. You do not need to do this to use this repo, it is simply for reference.

```bash
# clone prior art
git clone https://github.com/grantslatton/llama.cpp
cd llama.cpp

# update to latest
git remote add upstream https://github.com/ggerganov/llama.cpp
git fetch upstream

# create patch
git diff upstream/master > ../limited-llama/cfg.patch

# start a new repo and add the patch and upstream repo as a subtree

# add as subtree
git subtree add --prefix=llama.cpp https://github.com/ggerganov/llama.cpp master

# apply patch to 
git apply -v --directory llama.cpp cfg.patch
```