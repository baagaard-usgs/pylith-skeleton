// -*- web -*-
//
// This code is part of PyLith, developed through the Computational Infrastructure
// for Geodynamics (https://github.com/geodynamics/pylith).


// the controls and status regions of the launch panel, each reading the shared job state
// through {useJob} (notes/launch-local-spec.md section 3)
import { Controls } from './controls'
import { Status } from './status'


// publish the two regions under one name, so the layout composes them as {Job.Controls} and
// {Job.Status}
export const Job = { Controls, Status }


// end of file
