# Unity HPC

- Before writing a Slurm job or requesting an allocation, calculate a lower
  bound for host RAM, VRAM, GPU count, and wall time. Account for weights
  (parameter count × bytes per parameter), the largest batch and its tensors
  and caches, saved outputs, model loading, and the number of forwards. Include
  framework overhead and headroom when choosing the smallest viable request.
  Use CPU-only jobs for steps that need no GPU. Use a small measured pilot to
  refine runtime and peak memory estimates before scaling up.
- Keep the local and Unity checkouts clean and in sync. Use Git to transfer the
  same commit and verify the commit and working-tree status on both hosts. Keep
  logs, weights, temporary environments, and run outputs outside tracked
  source. Reuse an existing uv environment when its dependencies are compatible.
- Split work where artifacts allow it. Run independent sweeps in small shards,
  keep CPU fitting and analysis apart from expensive GPU inference when
  practical, and collect the outputs with their configuration and provenance.
  Use resumable outputs so a queued or preempted job can reuse completed work.
