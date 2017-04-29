import React, { Component } from 'react'
import { Alert } from 'react-bootstrap'
import RollDetail from './RollDetail'
import LeaveSlipDetail from './LeaveSlipDetail'
import GroupSlipDetail from './GroupSlipDetail'

const Summary = ({...p}) => {
  let unexcused_absences=p.eventsRolls.filter(esr => esr.event.status.roll==='absent'&&esr.event.status.slip!=='approved')
  let unexcused_tardies=p.eventsRolls.filter(esr => esr.event.status.roll==='tardy'&&esr.event.status.slip!=='approved')
  let excused_absences=p.eventsRolls.filter(esr => esr.event.status.roll==='absent'&&esr.event.status.slip==='approved')
  let excused_tardies=p.eventsRolls.filter(esr => esr.event.status.roll==='tardy'&&esr.event.status.slip==='approved')
  return (
    <div>
      <div className="legend">
        <div className="tardy">Tardy</div>
        <div className="absent">Absent</div>
        <div className="tardy-ls">Pending <br/> LS Tardy</div>
        <div className="absent-ls">Pending <br/> LS Absent</div>
        <div className="tardy-ap">Excused Tardy</div>
        <div className="absent-ap">Excused Absence</div>
      </div>
      <h5>Life Studies Possible: {p.eventsRolls.length}</h5>
      <h5>TOTAL</h5>
        <div className="row roll__table">
          <div className="col-md-4 roll__table roll__table--absent">Unexcused Absences</div>
          <div className="col-md-2">{unexcused_absences.length}</div>
          <div className="col-md-4 roll__table roll__table--present">Leave-Slips</div>
          <div className="col-md-2">{p.leaveslips.length}</div>
        </div>
        <div className="row roll__table">
          <div className="col-md-4 roll__table roll__table--tardy">Unexcused Tardies</div>
          <div className="col-md-2">{unexcused_tardies.length}</div>
          <div className="col-md-4 roll__table roll__table--present">Group-Slips</div>
          <div className="col-md-2">{p.groupslips.length}</div>
        </div>
        <div className="row roll__table">
          <div className="col-md-4 roll__table roll__table--tardy">Excused Absences</div>
          <div className="col-md-2">{excused_absences.length}</div>
        </div>
        <div className="row roll__table">
          <div className="col-md-4 roll__table roll__table--tardy">Excused Tardies</div>
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
    <Alert bsStyle="danger" className="dt-leaveslip__note">
      Note: Report information will not be up-to-date until attendance office hours (i.e., when the potential violators list is posted).
    </Alert>
    </div>
  )
}

Summary.propTypes = {
}

export default Summary
