import React, { PropTypes } from 'react'
import { Alert } from 'react-bootstrap'
import RollDetail from './RollDetail'
import LeaveSlipDetail from './LeaveSlipDetail'
import GroupSlipDetail2 from './GroupSlipDetail2'
import GroupSlipDetail from './GroupSlipDetail'

const Summary = ({...p}) => {
  let unexcused_absences=p.eventsRolls.filter(esr => esr.event.status.roll==='absent'&&esr.event.status.slip!=='approved').length
  let unexcused_tardies=p.eventsRolls.filter(esr => esr.event.status.roll==='tardy'&&esr.event.status.slip!=='approved').length
  let excused_absences=p.eventsRolls.filter(esr => esr.event.status.roll==='absent'&&esr.event.status.slip==='approved').length
  let excused_tardies=p.eventsRolls.filter(esr => esr.event.status.roll==='tardy'&&esr.event.status.slip==='approved').length
  return (
    <div>
      <h5>Life Studies Possible: {p.eventsRolls.length}</h5>
      <h5>Total</h5>
        <div className="row roll__table">
          <div className="col-md-4 roll__table roll__table--absent row">Unexcused Absences</div>
          <div className="col-md-2">{unexcused_absences}</div>
          <div className="col-md-4 roll__table roll__table--present row">Leave-Slips</div>
          <div className="col-md-2">{p.leaveslips.length}</div>
        </div>
        <div className="row roll__table">
          <div className="col-md-4 roll__table roll__table--tardy row">Unexcused Tardies</div>
          <div className="col-md-2">{unexcused_tardies}</div>
          <div className="col-md-4 roll__table roll__table--present row">Group-Slips</div>
          <div className="col-md-2">{p.groupslips.length}</div>
        </div>
        <div className="row roll__table">
          <div className="col-md-4 roll__table roll__table--tardy row">Excused Absences</div>
          <div className="col-md-2">{excused_absences}</div>
        </div>
        <div className="row roll__table">
          <div className="col-md-4 roll__table roll__table--tardy row">Excused Tardies</div>
          <div className="col-md-2">{excused_tardies}</div>
        </div>
      <h5>Unexcused Absences</h5>
        <div className="row roll__table">
          <div className="col-md-3">Date</div>
          <div className="col-md-3">Event</div>
          <div className="col-md-3">Status</div>
          <div className="col-md-3">Leave-Slip</div>
        </div>
      <h5>Rolls</h5>
        <h4>Unexcused Absences</h4>
          <div className="row roll__table"></div>
            {p.eventsRolls.filter(esr => esr.event.status.roll==='absent'&&esr.event.status.slip!=='approved').map(esr =>
              <RollDetail key={esr.event.start}
                {...esr}
              />
            )}
        <h4>Unexcused Tardies</h4>
          <div className="row roll__table"></div>
            {p.eventsRolls.filter(esr => esr.event.status.roll==='tardy'&&esr.event.status.slip!=='approved').map(esr =>
              <RollDetail key={esr.event.start}
                {...esr}
              />
            )}
        <h4>Excused Absences/Tardies</h4>
          <div className="row roll__table"></div>
            {p.eventsRolls.filter(esr => esr.event.status.slip==='approved').map(esr =>
              <RollDetail key={esr.event.start}
                {...esr}
              />
            )}
      <h5>Leave Slips</h5>
        <h4>Pending</h4>
          <div className="row roll__table"></div>
            {p.leaveslips.filter(ls => ls.status==='P').map(ls =>
              <LeaveSlipDetail key={ls.id}
                ls={ls}
                deleteSlip={(ls) => p.deleteSlip(ls)}
              />
            )}
        <h4>Denied</h4>
          <div className="row roll__table"></div>
            {p.leaveslips.filter(ls => ls.status==='D'||ls.status==='F').map(ls =>
              <LeaveSlipDetail key={ls.id}
                ls={ls}
                deleteSlip={(ls) => p.deleteSlip(ls)}
              />
            )}
        <h4>Approved</h4>
          <div className="row roll__table"></div>
            {p.leaveslips.filter(ls => ls.status==='A'||ls.status==='S').map(ls =>
              <LeaveSlipDetail key={ls.id}
                ls={ls}
                deleteSlip={(ls) => p.deleteSlip(ls)}
              />
            )}
      <h5>Group Leave Slips</h5>
        <h4>Pending</h4>
          <div className="row roll__table"></div>
            {p.groupslips.filter(gls => gls.status==='P').map(gls => 
            <GroupSlipDetail2 key={gls.id}
              gls={gls}
            />
            )}
      <h4>Denied</h4>
          <div className="row roll__table"></div>
            {p.groupslips.filter(gls => gls.status==='D'||gls.status==='F').map(gls => 
            <GroupSlipDetail2 key={gls.id}
              gls={gls}
            />
            )}
      <h4>Approved</h4>
          <div className="row roll__table"></div>
            {p.groupslips.filter(gls => gls.status==='A'||gls.status==='S').map(gls => 
            <GroupSlipDetail2 key={gls.id}
              gls={gls}
            />
            )}
    <Alert bsStyle="danger">
      Note: Report information will not be up-to-date until attendance office hours (i.e., when the potential violators list is posted).
    </Alert>
    </div>
  )
}

Summary.propTypes = {
}

export default Summary
