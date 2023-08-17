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

@pytest.mark.telemetry_files(source('BarrelShifter16.vhd'))
def test_BarrelShifter16():
    run(vhdl_sources=[source("BarrelShifter16.vhd")], toplevel="BarrelShifter16.vhd", module="logComb_cocotb" , testcase='tb_BarrelShifter16.vhd', toplevel_lang="vhdl")
    
@pytest.mark.telemetry_files(source('binarioToBcd.vhd'))
def test_binarioToBcd():
    run(vhdl_sources=[source("binarioToBcd.vhd")], toplevel="binarioToBcd.vhd", module="logComb_cocotb" , testcase='tb_binarioToBcd.vhd', toplevel_lang="vhdl")
    

@pytest.mark.telemetry_files(source('carrinho.vhd'))
def test_carrinho():
    run(vhdl_sources=[source("carrinho.vhd")], toplevel="carrinho.vhd", module="logComb_cocotb" , testcase='tb_carrinho.vhd', toplevel_lang="vhdl")
    
@pytest.mark.telemetry_files(source('circuito.vhd'))
def test_circuito():
    run(vhdl_sources=[source("circuito.vhd")], toplevel="circuito.vhd", module="logComb_cocotb" , testcase='tb_circuito.vhd', toplevel_lang="vhdl")
    
@pytest.mark.telemetry_files(source('ConceitoA.vhd'))
def test_ConceitoA():
    run(vhdl_sources=[source("ConceitoA.vhd")], toplevel="ConceitoA", module="logComb_cocotb" , testcase='tb_ConceitoA', toplevel_lang="vhdl")
    
@pytest.mark.telemetry_files(source('detectorDeMoedas.vhd'))
def test_detectorDeMoedas():
    run(vhdl_sources=[source("detectorDeMoedas.vhd")], toplevel="detectorDeMoedas", module="logComb_cocotb" , testcase='tb_detectorDeMoedas', toplevel_lang="vhdl")
    
@pytest.mark.telemetry_files(source('DMux2Way.vhd'))
def test_DMux2Way():
    run(vhdl_sources=[source("DMux2Way.vhd")], toplevel="DMux2Way", module="logComb_cocotb" , testcase='tb_DMux2Way', toplevel_lang="vhdl")
    
@pytest.mark.telemetry_files(source('DMux4Way.vhd'))
def test_DMux4Way():
    run(vhdl_sources=[source("DMux4Way.vhd")], toplevel="DMux4Way", module="logComb_cocotb" , testcase='tb_DMux4Way', toplevel_lang="vhdl")
    
@pytest.mark.telemetry_files(source('DMux8Way.vhd'))
def test_DMux8Way():
    run(vhdl_sources=[source("DMux8Way.vhd")], toplevel="DMux8Way", module="logComb_cocotb" , testcase='tb_DMux8Way', toplevel_lang="vhdl")
 
@pytest.mark.telemetry_files(source('impressora.vhd'))
def test_impressora():
    run(vhdl_sources=[source("impressora.vhd")], toplevel="impressora", module="logComb_cocotb" , testcase='tb_impressora', toplevel_lang="vhdl")

@pytest.mark.telemetry_files(source('Mux16.vhd'))
def test_Mux16():
    run(vhdl_sources=[source("Mux16.vhd")], toplevel="Mux16", module="logComb_cocotb" , testcase='tb_Mux16', toplevel_lang="vhdl")

@pytest.mark.telemetry_files(source('Mux2Way.vhd'))
def test_Mux2Way():
    run(vhdl_sources=[source("Mux2Way.vhd")], toplevel="Mux2Way", module="logComb_cocotb" , testcase='tb_Mux2Way', toplevel_lang="vhdl")

@pytest.mark.telemetry_files(source('Mux4Way16.vhd'))
def test_Mux4Way16():
    run(vhdl_sources=[source("Mux4Way16.vhd")], toplevel="Mux4Way16", module="logComb_cocotb" , testcase='tb_Mux4Way16', toplevel_lang="vhdl")


@pytest.mark.telemetry_files(source('Mux4Way.vhd'))
def test_Mux4Way():
    run(vhdl_sources=[source("Mux4Way.vhd")], toplevel="Mux4Way", module="logComb_cocotb" , testcase='tb_Mux4Way', toplevel_lang="vhdl")


@pytest.mark.telemetry_files(source('Mux8Way16.vhd'))
def test_Mux8Way16():
    run(vhdl_sources=[source("Mux8Way16.vhd")], toplevel="Mux8Way16", module="logComb_cocotb" , testcase='tb_Mux8Way16', toplevel_lang="vhdl")


@pytest.mark.telemetry_files(source('Mux8Way.vhd'))
def test_Mux8Way():
    run(vhdl_sources=[source("Mux8Way.vhd")], toplevel="Mux8Way", module="logComb_cocotb" , testcase='tb_Mux8Way', toplevel_lang="vhdl")


@pytest.mark.telemetry_files(source('Nand2.vhd'))
def test_Nand2():
    run(vhdl_sources=[source("Nand2.vhd")], toplevel="Nand2", module="logComb_cocotb" , testcase='tb_Nand2', toplevel_lang="vhdl")

@pytest.mark.telemetry_files(source('Nor8Way.vhd'))
def test_Nor8Way():
    run(vhdl_sources=[source("Nor8Way.vhd")], toplevel="Nor8Way", module="logComb_cocotb" , testcase='tb_Nor8Way', toplevel_lang="vhdl")


 
@pytest.mark.telemetry_files(source('Not16.vhd'), source('And16.vhd'))
def test_Not16():
    run(vhdl_sources=[source("Not16.vhd")], toplevel="Not16", module="logComb_cocotb" , testcase='tb_Not16', toplevel_lang="vhdl")
   

@pytest.mark.telemetry_files(source('Or16vhd'))
def test_Or16():
    run(vhdl_sources=[source("Or16.vhd")], toplevel="Or16.vhd", module="logComb_cocotb" , testcase='tb_Or16', toplevel_lang="vhdl")


@pytest.mark.telemetry_files(source('Or8Way.vhd'))
def test_Or8Way():
    run(vhdl_sources=[source("Or8Way.vhd")], toplevel="Or8Way.vhd", module="logComb_cocotb" , testcase='tb_Or8Way', toplevel_lang="vhdl")



@pytest.mark.telemetry_files(source('sevenSeg.vhd'))
def test_sevenSeg():
    run(vhdl_sources=[source("sevenSeg.vhd")], toplevel="sevenSeg.vhd", module="logComb_cocotb" , testcase='tb_sevenSeg', toplevel_lang="vhdl")



@pytest.mark.telemetry_files(source('xor3.vhd'))
def test_xor3():
    run(vhdl_sources=[source("xor3.vhd")], toplevel="sevenSeg.vhd", module="logComb_cocotb" , testcase='tb_xor3', toplevel_lang="vhdl")



  
if __name__ == "__main__":
    test_xor3()

