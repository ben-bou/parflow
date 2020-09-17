#---------------------------------------------------------
#  This runs the basic default_richards test case.
#  This run, as written in this input file, should take
#  3 nonlinear iterations.
#---------------------------------------------------------

from parflow import Run
from parflow.tools.fs import cp

vgf = Run("van-genuchten-file", __file__)

#---------------------------------------------------------
# Copying parameter files
#---------------------------------------------------------

cp('$PF_SRC/test/input/van-genuchten-alpha.pfb')
cp('$PF_SRC/test/input/van-genuchten-n.pfb')
cp('$PF_SRC/test/input/van-genuchten-sr.pfb')
cp('$PF_SRC/test/input/van-genuchten-ssat.pfb')

#---------------------------------------------------------

vgf.FileVersion = 4

vgf.Process.Topology.P = 1
vgf.Process.Topology.Q = 1
vgf.Process.Topology.R = 1

#---------------------------------------------------------
# Computational Grid
#---------------------------------------------------------

vgf.ComputationalGrid.Lower.X = -10.0
vgf.ComputationalGrid.Lower.Y = 10.0
vgf.ComputationalGrid.Lower.Z = 1.0

vgf.ComputationalGrid.DX = 8.8888888888888893
vgf.ComputationalGrid.DY = 10.666666666666666
vgf.ComputationalGrid.DZ = 1.0

vgf.ComputationalGrid.NX = 10
vgf.ComputationalGrid.NY = 10
vgf.ComputationalGrid.NZ = 8

#---------------------------------------------------------
# The Names of the GeomInputs
#---------------------------------------------------------

vgf.GeomInput.Names = 'domain_input background_input source_region_input concen_region_input'

#---------------------------------------------------------
# Domain Geometry Input
#---------------------------------------------------------

vgf.GeomInput.domain_input.InputType = 'Box'
vgf.GeomInput.domain_input.GeomName = 'domain'

#---------------------------------------------------------
# Domain Geometry
#---------------------------------------------------------

vgf.Geom.domain.Lower.X = -10.0
vgf.Geom.domain.Lower.Y = 10.0
vgf.Geom.domain.Lower.Z = 1.0

vgf.Geom.domain.Upper.X = 150.0
vgf.Geom.domain.Upper.Y = 170.0
vgf.Geom.domain.Upper.Z = 9.0

vgf.Geom.domain.Patches = 'left right front back bottom top'

#---------------------------------------------------------
# Background Geometry Input
#---------------------------------------------------------

vgf.GeomInput.background_input.InputType = 'Box'
vgf.GeomInput.background_input.GeomName = 'background'

#---------------------------------------------------------
# Background Geometry
#---------------------------------------------------------

vgf.Geom.background.Lower.X = -99999999.0
vgf.Geom.background.Lower.Y = -99999999.0
vgf.Geom.background.Lower.Z = -99999999.0

vgf.Geom.background.Upper.X = 99999999.0
vgf.Geom.background.Upper.Y = 99999999.0
vgf.Geom.background.Upper.Z = 99999999.0

#---------------------------------------------------------
# Source_Region Geometry Input
#---------------------------------------------------------

vgf.GeomInput.source_region_input.InputType = 'Box'
vgf.GeomInput.source_region_input.GeomName = 'source_region'

#---------------------------------------------------------
# Source_Region Geometry
#---------------------------------------------------------

vgf.Geom.source_region.Lower.X = 65.56
vgf.Geom.source_region.Lower.Y = 79.34
vgf.Geom.source_region.Lower.Z = 4.5

vgf.Geom.source_region.Upper.X = 74.44
vgf.Geom.source_region.Upper.Y = 89.99
vgf.Geom.source_region.Upper.Z = 5.5

#---------------------------------------------------------
# Concen_Region Geometry Input
#---------------------------------------------------------

vgf.GeomInput.concen_region_input.InputType = 'Box'
vgf.GeomInput.concen_region_input.GeomName = 'concen_region'

#---------------------------------------------------------
# Concen_Region Geometry
#---------------------------------------------------------

vgf.Geom.concen_region.Lower.X = 60.0
vgf.Geom.concen_region.Lower.Y = 80.0
vgf.Geom.concen_region.Lower.Z = 4.0

vgf.Geom.concen_region.Upper.X = 80.0
vgf.Geom.concen_region.Upper.Y = 100.0
vgf.Geom.concen_region.Upper.Z = 6.0

#-----------------------------------------------------------------------------
# Perm
#-----------------------------------------------------------------------------

vgf.Geom.Perm.Names = 'background'

vgf.Geom.background.Perm.Type = 'Constant'
vgf.Geom.background.Perm.Value = 4.0

vgf.Perm.TensorType = 'TensorByGeom'

vgf.Geom.Perm.TensorByGeom.Names = 'background'

vgf.Geom.background.Perm.TensorValX = 1.0
vgf.Geom.background.Perm.TensorValY = 1.0
vgf.Geom.background.Perm.TensorValZ = 1.0

#-----------------------------------------------------------------------------
# Specific Storage
#-----------------------------------------------------------------------------

vgf.SpecificStorage.Type = 'Constant'
vgf.SpecificStorage.GeomNames = 'domain'
vgf.Geom.domain.SpecificStorage.Value = 1.0e-4

#-----------------------------------------------------------------------------
# Phases
#-----------------------------------------------------------------------------

vgf.Phase.Names = 'water'

vgf.Phase.water.Density.Type = 'Constant'
vgf.Phase.water.Density.Value = 1.0

vgf.Phase.water.Viscosity.Type = 'Constant'
vgf.Phase.water.Viscosity.Value = 1.0

#-----------------------------------------------------------------------------
# Contaminants
#-----------------------------------------------------------------------------

vgf.Contaminants.Names = ''

#-----------------------------------------------------------------------------
# Retardation
#-----------------------------------------------------------------------------

vgf.Geom.Retardation.GeomNames = ''

#-----------------------------------------------------------------------------
# Gravity
#-----------------------------------------------------------------------------

vgf.Gravity = 1.0

#-----------------------------------------------------------------------------
# Setup timing info
#-----------------------------------------------------------------------------

vgf.TimingInfo.BaseUnit = 1.0
vgf.TimingInfo.StartCount = 0
vgf.TimingInfo.StartTime = 0.0
vgf.TimingInfo.StopTime = 0.010
vgf.TimingInfo.DumpInterval = -1
vgf.TimeStep.Type = 'Constant'
vgf.TimeStep.Value = 0.001

#-----------------------------------------------------------------------------
# Porosity
#-----------------------------------------------------------------------------

vgf.Geom.Porosity.GeomNames = 'background'

vgf.Geom.background.Porosity.Type = 'Constant'
vgf.Geom.background.Porosity.Value = 1.0

#-----------------------------------------------------------------------------
# Domain
#-----------------------------------------------------------------------------

vgf.Domain.GeomName = 'domain'

#-----------------------------------------------------------------------------
# Relative Permeability
#-----------------------------------------------------------------------------

vgf.Phase.RelPerm.Type = 'VanGenuchten'
vgf.Phase.RelPerm.GeomNames = 'domain'

vgf.Phase.RelPerm.VanGenuchten.File = 1
vgf.Geom.domain.RelPerm.Alpha.Filename = 'van-genuchten-alpha.pfb'
vgf.Geom.domain.RelPerm.N.Filename = 'van-genuchten-n.pfb'

#---------------------------------------------------------
# Saturation
#---------------------------------------------------------

vgf.Phase.Saturation.Type = 'VanGenuchten'
vgf.Phase.Saturation.GeomNames = 'domain'

vgf.Geom.domain.Saturation.Alpha = 0.005
vgf.Geom.domain.Saturation.N = 2.0
vgf.Geom.domain.Saturation.SRes = 0.2
vgf.Geom.domain.Saturation.SSat = 0.99

vgf.Phase.Saturation.VanGenuchten.File = 1
vgf.Geom.domain.Saturation.Alpha.Filename = 'van-genuchten-alpha.pfb'
vgf.Geom.domain.Saturation.N.Filename = 'van-genuchten-n.pfb'
vgf.Geom.domain.Saturation.SRes.Filename = 'van-genuchten-sr.pfb'
vgf.Geom.domain.Saturation.SSat.Filename = 'van-genuchten-ssat.pfb'

#-----------------------------------------------------------------------------
# Wells
#-----------------------------------------------------------------------------

vgf.Wells.Names = ''

#-----------------------------------------------------------------------------
# Time Cycles
#-----------------------------------------------------------------------------

vgf.Cycle.Names = 'constant'
vgf.Cycle.constant.Names = 'alltime'
vgf.Cycle.constant.alltime.Length = 1
vgf.Cycle.constant.Repeat = -1

#-----------------------------------------------------------------------------
# Boundary Conditions: Pressure
#-----------------------------------------------------------------------------

vgf.BCPressure.PatchNames = 'left right front back bottom top'

vgf.Patch.left.BCPressure.Type = 'DirEquilRefPatch'
vgf.Patch.left.BCPressure.Cycle = 'constant'
vgf.Patch.left.BCPressure.RefGeom = 'domain'
vgf.Patch.left.BCPressure.RefPatch = 'bottom'
vgf.Patch.left.BCPressure.alltime.Value = 5.0

vgf.Patch.right.BCPressure.Type = 'DirEquilRefPatch'
vgf.Patch.right.BCPressure.Cycle = 'constant'
vgf.Patch.right.BCPressure.RefGeom = 'domain'
vgf.Patch.right.BCPressure.RefPatch = 'bottom'
vgf.Patch.right.BCPressure.alltime.Value = 3.0

vgf.Patch.front.BCPressure.Type = 'FluxConst'
vgf.Patch.front.BCPressure.Cycle = 'constant'
vgf.Patch.front.BCPressure.alltime.Value = 0.0

vgf.Patch.back.BCPressure.Type = 'FluxConst'
vgf.Patch.back.BCPressure.Cycle = 'constant'
vgf.Patch.back.BCPressure.alltime.Value = 0.0

vgf.Patch.bottom.BCPressure.Type = 'FluxConst'
vgf.Patch.bottom.BCPressure.Cycle = 'constant'
vgf.Patch.bottom.BCPressure.alltime.Value = 0.0

vgf.Patch.top.BCPressure.Type = 'FluxConst'
vgf.Patch.top.BCPressure.Cycle = 'constant'
vgf.Patch.top.BCPressure.alltime.Value = 0.0

#---------------------------------------------------------
# Topo slopes in x-direction
#---------------------------------------------------------

vgf.TopoSlopesX.Type = 'Constant'
vgf.TopoSlopesX.GeomNames = 'domain'
vgf.TopoSlopesX.Geom.domain.Value = 0.0

#---------------------------------------------------------
# Topo slopes in y-direction
#---------------------------------------------------------

vgf.TopoSlopesY.Type = 'Constant'
vgf.TopoSlopesY.GeomNames = 'domain'
vgf.TopoSlopesY.Geom.domain.Value = 0.0

#---------------------------------------------------------
# Mannings coefficient
#---------------------------------------------------------

vgf.Mannings.Type = 'Constant'
vgf.Mannings.GeomNames = 'domain'
vgf.Mannings.Geom.domain.Value = 0.

#---------------------------------------------------------
# Initial conditions: water pressure
#---------------------------------------------------------

vgf.ICPressure.Type = 'HydroStaticPatch'
vgf.ICPressure.GeomNames = 'domain'
vgf.Geom.domain.ICPressure.Value = 3.0
vgf.Geom.domain.ICPressure.RefGeom = 'domain'
vgf.Geom.domain.ICPressure.RefPatch = 'bottom'

#-----------------------------------------------------------------------------
# Phase sources:
#-----------------------------------------------------------------------------

vgf.PhaseSources.water.Type = 'Constant'
vgf.PhaseSources.water.GeomNames = 'background'
vgf.PhaseSources.water.Geom.background.Value = 0.0


#-----------------------------------------------------------------------------
# Exact solution specification for error calculations
#-----------------------------------------------------------------------------

vgf.KnownSolution = 'NoKnownSolution'

#-----------------------------------------------------------------------------
# Set solver parameters
#-----------------------------------------------------------------------------

vgf.Solver = 'Richards'
vgf.Solver.MaxIter = 5

vgf.Solver.Nonlinear.MaxIter = 10
vgf.Solver.Nonlinear.ResidualTol = 1e-9
vgf.Solver.Nonlinear.EtaChoice = 'EtaConstant'
vgf.Solver.Nonlinear.EtaValue = 1e-5
vgf.Solver.Nonlinear.UseJacobian = True
vgf.Solver.Nonlinear.DerivativeEpsilon = 1e-2

vgf.Solver.Linear.KrylovDimension = 10

vgf.Solver.Linear.Preconditioner = 'PFMG'

#-----------------------------------------------------------------------------
# Run and Unload the ParFlow output files
#-----------------------------------------------------------------------------

vgf.dist('van-genuchten-alpha.pfb')
vgf.dist('van-genuchten-n.pfb')
vgf.dist('van-genuchten-sr.pfb')
vgf.dist('van-genuchten-ssat.pfb')

vgf.run()
