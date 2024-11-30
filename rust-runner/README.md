# Advent of CodSpeed - Rust Runner

## Testing that your Rust solution will be picked up by the runner

1. Clone this repository
1. Add your input file in this directory named `input.txt`
1. Bind this runner to your solution:
   - For regular repositories, run:
     ```
     cargo add --git <YOUR_REPO_URL> --rename solution
     ```
   - If you specified a sub crate when you registered your solution, run:
     ```
     cargo add --git <YOUR_REPO_URL> --package <YOUR_CRATE_NAME> --rename solution
     ```
1. If you specified a toolchain while registering your solution, set it in the
   `rust-toolchain.toml` file:
   ```
   [toolchain]
   channel = "<YOUR TOOLCHAIN GOES HERE>"
   ```
1. Select the day by changing it in bench.rs line 3. Replace `<day_number>` with the day you wanna test. (`day1`, `day2`, `day13`, etc.)
1. Install `cargo-codspeed`:
   ```
   cargo binstall cargo-codspeed
   ```
   (make sure you have `cargo-binstall` installed, if not, run `cargo install cargo-binstall`)
1. Build the benchmarks:

   ```
   cargo codspeed build
   ```

1. Run the benchmarks locally (without instrumentation):

   ```
   cargo codspeed run
   ```

If you don't see any errors, your solution is ready to be picked up by the runner and you will see the results on the leaderboard.
