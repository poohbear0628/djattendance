import React, { PropTypes } from 'react'
import { Alert } from 'react-bootstrap'
import RollDetail from './RollDetail'
import LeaveSlipDetail from './LeaveSlipDetail'
import GroupSlipDetail2 from './GroupSlipDetail2'
import GroupSlipDetail from './GroupSlipDetail'

const Summary = ({...p}) => {
  let unexcused_absences=p.eventsRolls.filter(esr => esr.event.status.roll==='absent'&&esr.event.status.slip!=='approved')
  let unexcused_tardies=p.eventsRolls.filter(esr => esr.event.status.roll==='tardy'&&esr.event.status.slip!=='approved')
  let excused_absences=p.eventsRolls.filter(esr => esr.event.status.roll==='absent'&&esr.event.status.slip==='approved')
  let excused_tardies=p.eventsRolls.filter(esr => esr.event.status.roll==='tardy'&&esr.event.status.slip==='approved')
  return (
    <div>
      <h5>Life Studies Possible: {p.eventsRolls.length}</h5>
      <h5>TOTAL</h5>
        <div className="row roll__table">
          <div className="col-md-4 roll__table roll__table--absent row">Unexcused Absences</div>
          <div className="col-md-2">{unexcused_absences.length}</div>
          <div className="col-md-4 roll__table roll__table--present row">Leave-Slips</div>
          <div className="col-md-2">{p.leaveslips.length}</div>
        </div>
        <div className="row roll__table">
          <div className="col-md-4 roll__table roll__table--tardy row">Unexcused Tardies</div>
          <div className="col-md-2">{unexcused_tardies.length}</div>
          <div className="col-md-4 roll__table roll__table--present row">Group-Slips</div>
          <div className="col-md-2">{p.groupslips.length}</div>
        </div>
        <div className="row roll__table">
          <div className="col-md-4 roll__table roll__table--tardy row">Excused Absences</div>
          <div className="col-md-2">{excused_absences.length}</div>
        </div>
        <div className="row roll__table">
          <div className="col-md-4 roll__table roll__table--tardy row">Excused Tardies</div>
          <div className="col-md-2">{excused_tardies.length}</div>
        </div>
      <h5>UNEXCUSED ABSENCES</h5>
        <div className="row roll__table">
          <div className="col-md-2">DATE</div>
          <div className="col-md-4">EVENT</div>
          <div className="col-md-3">STATUS</div>
          <div className="col-md-3">LEAVE-SLIP</div>
        </div>
        <div className="row roll__table"></div>
            {unexcused_absences.map(esr =>
              <RollDetail key={esr.event.start}
                {...esr}
              />
            )}
      <h5>UNEXCUSED TARDIES</h5>
        <div className="row roll__table">
          <div className="col-md-2">DATE</div>
          <div className="col-md-4">EVENT</div>
          <div className="col-md-3">STATUS</div>
          <div className="col-md-3">LEAVE-SLIP</div>
        </div>
        <div className="row roll__table"></div>
            {unexcused_tardies.map(esr =>
              <RollDetail key={esr.event.start}
                {...esr}
              />
            )}
    </div>
  )
}

Summary.propTypes = {
}

export default Summary
