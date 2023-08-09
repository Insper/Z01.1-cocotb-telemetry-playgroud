from cocotb_test.simulator import run
import pytest
import os

from telemetry import telemetryMark
pytestmark = telemetryMark()


def source(name):
	dir = os.path.dirname(__file__)
	src_dir = os.path.join(dir, 'src' )
	return os.path.join(src_dir, name)

@pytest.mark.telemetry_files(source('and16.vhd'))
def test_and16():
    run(vhdl_sources=[source("and16.vhd")], toplevel="and16", module="logComb_cocotb" , testcase='tb_and16', toplevel_lang="vhdl")

@pytest.mark.telemetry_files(source('not16.vhd'), source('and16.vhd'))
def test_not16():
    run(vhdl_sources=[source("not16.vhd")], toplevel="not16", module="logComb_cocotb" , testcase='tb_not16', toplevel_lang="vhdl")
    
if __name__ == "__main__":
    test_and16()

