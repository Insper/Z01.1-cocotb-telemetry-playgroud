from cocotb_test.simulator import run
import pytest
import os

from telemetry import telemetryMark
pytestmark = telemetryMark()


def source(name):
	dir = os.path.dirname(__file__)
	src_dir = os.path.join(dir, 'src' )
	return os.path.join(src_dir, name)


@pytest.mark.telemetry_files(source('conceito_a/flipflopjk.vhd'))
def test_flipflopjk():
    run(vhdl_sources=[source("conceito_a/flipflopjk.vhd")], toplevel="flipflopjk", module="logseq_cocotb" , testcase='tb_flipflopjk', toplevel_lang="vhdl")

@pytest.mark.telemetry_files(source('conceito_a/flipflopt.vhd'))
def test_flipflopt():
    run(vhdl_sources=[source("conceito_a/flipflopt.vhd")], toplevel="flipflopt", module="logseq_cocotb" , testcase='tb_flipflopt', toplevel_lang="vhdl")

@pytest.mark.telemetry_files(source('conceito_a/counterdown.vhd'),source('conceito_a/flipflopt.vhd'))
def test_counterdown():
    run(vhdl_sources=[source('conceito_a/counterdown.vhd'),source("conceito_a/flipflopt.vhd")], toplevel="counterdown", module="logseq_cocotb" , testcase='tb_counterdown', toplevel_lang="vhdl")



@pytest.mark.telemetry_files(source('flipflopd.vhd'))
def test_flipflopd():
    run(vhdl_sources=[source("flipflopd.vhd")], toplevel="flipflopd", module="logseq_cocotb" , testcase='tb_flipflopd', toplevel_lang="vhdl")


@pytest.mark.telemetry_files(source('binarydigit.vhd'),source('flipflopd.vhd'),source('mux2way.vhd'))
def test_binarydigit():
    run(vhdl_sources=[source("binarydigit.vhd"),source('flipflopd.vhd'),source('../../b_logComb/src/mux2way.vhd')], toplevel="binarydigit", module="logseq_cocotb" , testcase='tb_binarydigit', toplevel_lang="vhdl")


@pytest.mark.telemetry_files(source('register8.vhd'),source('binarydigit.vhd'),source('flipflopd.vhd'),source('../../b_logComb/src/mux2way.vhd'))
def test_register8():
    run(vhdl_sources=[source('register8.vhd'),source("binarydigit.vhd"),source('flipflopd.vhd'),source('../../b_logComb/src/mux2way.vhd')], toplevel="register8", module="logseq_cocotb" , testcase='tb_register8', toplevel_lang="vhdl")



if __name__ == "__main__":
    test_flipflopd()

