from cocotb_test.simulator import run
import pytest
import os

from telemetry import telemetryMark
pytestmark = telemetryMark()


def source(name):
	dir = os.path.dirname(__file__)
	src_dir = os.path.join(dir, 'src' )
	return os.path.join(src_dir, name)

@pytest.mark.telemetry_files(source('Add16.vhd'))
def test_Add16():
    run(vhdl_sources=[source("Add16.vhd")], toplevel="Add16", module="ula_cocotb" , testcase='tb_Add16', toplevel_lang="vhdl")


@pytest.mark.telemetry_files(source('HalfAdder.vhd'))
def test_HalfAdder():
    run(vhdl_sources=[source("HalfAdder.vhd")], toplevel="HalfAdder", module="ula_cocotb" , testcase='tb_HalfAdder', toplevel_lang="vhdl")



@pytest.mark.telemetry_files(source('FullAdder.vhd'))
def test_FullAdder():
    run(vhdl_sources=[source("FullAdder.vhd")], toplevel="FullAdder", module="ula_cocotb" , testcase='tb_FullAdder', toplevel_lang="vhdl")


@pytest.mark.telemetry_files(source('Inc16.vhd'))
def test_Inc16():
    run(vhdl_sources=[source("Inc16.vhd")], toplevel="Inc16", module="ula_cocotb" , testcase='tb_Inc16', toplevel_lang="vhdl")



@pytest.mark.telemetry_files(source('inversor16.vhd'))
def test_inversor16():
    run(vhdl_sources=[source("inversor16.vhd")], toplevel="inversor16", module="ula_cocotb" , testcase='tb_inversor16', toplevel_lang="vhdl")




@pytest.mark.telemetry_files(source('zerador16.vhd'))
def test_zerador16():
    run(vhdl_sources=[source("zerador16.vhd")], toplevel="zerador16", module="ula_cocotb" , testcase='tb_zerador16', toplevel_lang="vhdl")


@pytest.mark.telemetry_files(source('comparador16.vhd'))
def test_comparador16():
    run(vhdl_sources=[source("comparador16.vhd")], toplevel="comparador16", module="ula_cocotb" , testcase='tb_comparador16', toplevel_lang="vhdl")




@pytest.mark.telemetry_files(source('ALU.vhd'))
def test_ALU():
    run(vhdl_sources=[source("ALU.vhd")], toplevel="ALU", module="ula_cocotb" , testcase='tb_ALU', toplevel_lang="vhdl")




  
if __name__ == "__main__":
    test_ALU()

