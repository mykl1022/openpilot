import os
import subprocess
from common.basedir import BASEDIR
from pathlib import Path

CUSTOM_BOOT = "/data/params/d/CustomBootScreen"


class Spinner():
  def __init__(self):
    try:
      self.spinner_proc = subprocess.Popen(["./spinner"],
                                           stdin=subprocess.PIPE,
                                           cwd=os.path.join(BASEDIR, "selfdrive", "ui"),
                                           close_fds=True)
    except OSError:
      self.spinner_proc = None

  def __enter__(self):
    return self

  def update(self, spinner_text: str):
    if self.spinner_proc is not None:
      self.spinner_proc.stdin.write(spinner_text.encode('utf8') + b"\n")
      try:
        self.spinner_proc.stdin.flush()
      except BrokenPipeError:
        pass

  def update_progress(self, cur: float, total: float):
    self.update(str(round(100 * cur / total)))

  def close(self):
    if self.spinner_proc is not None:
      try:
        self.spinner_proc.stdin.close()
      except BrokenPipeError:
        pass
      self.spinner_proc.terminate()
      self.spinner_proc = None

  def __del__(self):
    self.close()

  def __exit__(self, exc_type, exc_value, traceback):
    self.close()


if __name__ == "__main__":
  import time
  custom_boot = Path(CUSTOM_BOOT)
  if custom_boot.is_file():
    with open(CUSTOM_BOOT) as f:
      if '1' in f.read():
        with Spinner() as s:
          s.update("m")
          time.sleep(1.0)
          s.update("ma")
          time.sleep(0.3)
          s.update("may")
          time.sleep(0.3)
          s.update("t")
          time.sleep(0.3)
          s.update("th")
          time.sleep(0.3)
          s.update("the")
          time.sleep(0.3)
          s.update("F")
          time.sleep(0.3)
          s.update("Fo")
          time.sleep(0.3)
          s.update("For")
          time.sleep(0.3)
          s.update("Forc")
          time.sleep(0.5)
          s.update("Force")
          time.sleep(0.5)
          s.update("Be")
          time.sleep(0.5)
          s.update("With")
          time.sleep(1.0)
          s.update("You...")
          time.sleep(2.0)
  else:
    with Spinner() as s:
      s.update("Spinner text")
      time.sleep(5.0)
    print("gone")
    time.sleep(5.0)
