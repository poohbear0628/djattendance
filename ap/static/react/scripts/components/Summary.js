import React, { PropTypes } from 'react'
import { Alert } from 'react-bootstrap'
import RollDetail from './RollDetail'
import LeaveSlipDetail from './LeaveSlipDetail'
import GroupSlipDetail from './GroupSlipDetail'

const Summary = ({...p}) => {
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
  		<h5>Roll Events</h5>
	    <table className='table table-condensed'>
	    	<tbody>
		    	<tr>
		    		<th>Date</th>
		    		<th>Event</th>
		    		<th>Status</th>
		    	</tr>
		      {p.eventsRolls.map(esr =>
		        <RollDetail key={esr.event.start}
		          {...esr}
		        />
		      )}
	      </tbody>
	    </table>
	    <h5>Leave Slips</h5>
    	<table className='table table-condensed'>
	    	<tbody>
		    	<tr>
		    		<th>Type</th>
		    		<th>Status</th>
		    		<th>Actions</th>
		    	</tr>
		      {p.leaveslips.map(ls =>
		        <LeaveSlipDetail key={ls.id}
		          ls={ls}
		          deleteSlip={(ls) => p.deleteSlip(ls)}
		        />
		      )}
	      </tbody>
	    </table>
	    <h5>Group Leave Slips</h5>
    	<table className='table table-condensed'>
	    	<tbody>
		    	<tr>
		    		<th>Type</th>
		    		<th>Status</th>
		    		<th>Actions</th>
		    	</tr>
		      {p.groupslips.map(gls =>
		        <GroupSlipDetail key={gls.id}
		          gls={gls}
		        />
		      )}
	      </tbody>
	    </table>
    <Alert bsStyle="danger">
      Note: Report information will not be up-to-date until attendance office hours (i.e., when the potential violators list is posted).
    </Alert>
    </div>
  )
}

Summary.propTypes = {
}

export default Summary
