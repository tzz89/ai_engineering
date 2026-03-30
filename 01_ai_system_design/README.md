# Ai System Design

## Generic System

                                         WAL   -> DB
                                          |
Client -> Gateway (Rate limiting) -> Session Manager -> message queue -> Inference Service
                                          |
                                        Redis




## functional requirements



## non functional requirements
1. Concurrent request
2. Latency
3. Throughput



## Components
1. Tools
   1. Search tool
2. Memory
   1. Short term
   2. Long term
3. KV cache (Usually handled by VLLM)
4. Vector database


## Lifecycle of a message
1. tokenization
2. convert to embeddings
3. transformer X N
4. Sampling
5. detokenization
6. convert to output


## Online references
1. https://www.youtube.com/watch?v=bAYtYz-3t6w (Deep understanding of of inference optimization, how group attention reduce the KV cache requirement)
