from cocotb_test.simulator import run
import pytest
import os

from telemetry import telemetryMark
pytestmark = telemetryMark()


def source(name):
	dir = os.path.dirname(__file__)
	src_dir = os.path.join(dir, 'src' )
	return os.path.join(src_dir, name)

@pytest.mark.telemetry_files(source('BinaryDigit.vhd'))
def test_BinaryDigit():
    run(vhdl_sources=[source("BinaryDigit.vhd")], toplevel="BinaryDigit", module="logSeq_cocotb" , testcase='tb_BinaryDigit', toplevel_lang="vhdl")


@pytest.mark.telemetry_files(source('FlipFlopD.vhd'))
def test_FlipFlopD():
    run(vhdl_sources=[source("FlipFlopD.vhd")], toplevel="FlipFlopD", module="logSeq_cocotb" , testcase='tb_FlipFlopD', toplevel_lang="vhdl")



@pytest.mark.telemetry_files(source('PC.vhd'))
def test_PC():
    run(vhdl_sources=[source("PC.vhd")], toplevel="PC", module="logSeq_cocotb" , testcase='tb_PC', toplevel_lang="vhdl")



@pytest.mark.telemetry_files(source('Register8.vhd'))
def test_Register8():
    run(vhdl_sources=[source("Register8.vhd")], toplevel="Register8", module="logSeq_cocotb" , testcase='tb_Register8', toplevel_lang="vhdl")



@pytest.mark.telemetry_files(source('Register16.vhd'))
def test_Register16():
    run(vhdl_sources=[source("Register16.vhd")], toplevel="Register16", module="logSeq_cocotb" , testcase='tb_Register16', toplevel_lang="vhdl")



@pytest.mark.telemetry_files(source('Register32.vhd'))
def test_Register32():
    run(vhdl_sources=[source("Register32.vhd")], toplevel="Register32", module="logSeq_cocotb" , testcase='tb_Register32', toplevel_lang="vhdl")




@pytest.mark.telemetry_files(source('Register64.vhd'))
def test_Register64():
    run(vhdl_sources=[source("Register64.vhd")], toplevel="Register64", module="logSeq_cocotb" , testcase='tb_Register64', toplevel_lang="vhdl")



@pytest.mark.telemetry_files(source('Ram8.vhd'))
def test_Ram8():
    run(vhdl_sources=[source("Ram8.vhd")], toplevel="Ram8", module="logSeq_cocotb" , testcase='tb_Ram8', toplevel_lang="vhdl")


@pytest.mark.telemetry_files(source('Ram64.vhd'))
def test_Ram64():
    run(vhdl_sources=[source("Ram64.vhd")], toplevel="Ram64", module="logSeq_cocotb" , testcase='tb_Ram64', toplevel_lang="vhdl")



@pytest.mark.telemetry_files(source('Ram512.vhd'))
def test_Ram512():
    run(vhdl_sources=[source("Ram512.vhd")], toplevel="Ram512", module="logSeq_cocotb" , testcase='tb_Ram512', toplevel_lang="vhdl")



@pytest.mark.telemetry_files(source('Ram4K.vhd'))
def test_Ram4K():
    run(vhdl_sources=[source("Ram4K.vhd")], toplevel="Ram4K", module="logSeq_cocotb" , testcase='tb_Ram4K', toplevel_lang="vhdl")


@pytest.mark.telemetry_files(source('CounterDown.vhd'))
def test_CounterDown():
    run(vhdl_sources=[source("CounterDown.vhd")], toplevel="CounterDown", module="logSeq_cocotb" , testcase='tb_CounterDown', toplevel_lang="vhdl")


@pytest.mark.telemetry_files(source('FlipFlopT.vhd'))
def test_FlipFlopT():
    run(vhdl_sources=[source("FlipFlopT.vhd")], toplevel="FlipFlopT", module="logSeq_cocotb" , testcase='tb_FlipFlopT', toplevel_lang="vhdl")


@pytest.mark.telemetry_files(source('FlipFlopJK.vhd'))
def test_FlipFlopJK():
    run(vhdl_sources=[source("FlipFlopJK.vhd")], toplevel="FlipFlopJK", module="logSeq_cocotb" , testcase='tb_FlipFlopJK', toplevel_lang="vhdl")


  
if __name__ == "__main__":
    test_FlipFlopJK()

