from program.sous_marin import SM, SMNuclear, PSM, MSM

def test_SMNuclear_class():
    smnuclear=SMNuclear() 
    assert smnuclear.size_x==0  
    assert smnuclear.size_y==0
    assert smnuclear.layer==2

def test_PSM_class():
    psm=PSM()
    assert psm.size_x==3
    assert psm.size_y==1
    assert psm.layer==2

def test_MSM_class():
    msm=MSM()
    assert msm.size_x==2
    assert msm.size_y==1
    assert msm.layer==2