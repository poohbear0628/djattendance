import React, { Component } from 'react'
import { Alert } from 'react-bootstrap'
import RollDetail from './RollDetail'
import LeaveSlipDetail from './LeaveSlipDetail'
import GroupSlipDetail from './GroupSlipDetail'
import { FA_ICON_LOOKUP } from '../constants'

const Summary = ({...p}) => {
  let unexcused_absences=p.eventsRolls.filter(esr => esr.event.status.roll==='absent'&&esr.event.status.slip!=='approved')
  let unexcused_tardies=p.eventsRolls.filter(esr => esr.event.status.roll==='tardy'&&esr.event.status.slip!=='approved')
  const TARDY_LIMIT = 4
  const ABSENT_LIMIT = 1
  let tardies = unexcused_tardies.length
  let absences = unexcused_absences.length
  let tardyLifestudies = tardies > TARDY_LIMIT  ? tardies - TARDY_LIMIT + 1 : 0
  let absentLifestudies = absences > ABSENT_LIMIT ? absences - ABSENT_LIMIT + 1 : 0
  return (
    <div>
      <div className="legend">
        <div className="tardy legend__tardy">Tardy</div>
        <div className="absent legend__absent">Absent</div>
        <div className="legend__leaveslip-pending">
          Slip Pending
          <div className="legend__slip"><i className={"pending fa fa-" + FA_ICON_LOOKUP['pending']} aria-hidden="true"></i></div>
        </div>
        <div className="legend__leaveslip-approved">
          Slip Approved
          <div className="legend__slip"><i className={"approved fa fa-" + FA_ICON_LOOKUP['approved']} aria-hidden="true"></i></div>
        </div>
        <div className="legend__leaveslip-denied">
          Slip Denied
          <div className="legend__slip"><i className={"denied fa fa-" + FA_ICON_LOOKUP['denied']} aria-hidden="true"></i></div>
        </div>
      </div>

      <h5>
        Life Studies Possible: {tardyLifestudies + absentLifestudies} (
          {absentLifestudies > 0 ? (<span>{absences} absences</span>) : ''}
          {absentLifestudies && tardyLifestudies ? ', ' : ''}
          {tardyLifestudies > 0 ? (<span>{tardies} tardies</span>) : ''}
        )
      </h5>

      <Alert bsStyle="danger" className="dt-leaveslip__note">
        Note: Report information will not be up-to-date until attendance office hours (i.e., when the potential violators list is posted).
      </Alert>
    </div>
  )
}

Summary.propTypes = {
}

export default Summary
