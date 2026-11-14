# Corvane Keystone Vector Cache

Reference implementation for the Keystone Vector Cache paper (RVLS 2026).

## Status

Released - v1.0.0. The complete implementation, the evaluation harness
and the sample datasets are included in this repository.

## Layout

- `src/` - cache and eviction implementations
- `data/` - sample embedding bundles
- `experiments/` - benchmark scripts used for the paper

## Quick start

```bash
python experiments/bench.py --config data/bench_config.json
```

Licensed under Apache-2.0.
