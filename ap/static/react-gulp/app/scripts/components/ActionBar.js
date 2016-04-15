import React, { PropTypes } from 'react'
import { Button, Collapse, OverlayTrigger, Popover } from 'react-bootstrap'
import SelectedEvent from './SelectedEvent'
import RollSlipForm from './RollSlipForm'

const ActionBar = ({submitRollShow, submitLeaveSlipShow, submitGroupLeaveSlipShow, otherReasonsShow, selectedEvents, formSuccess, trainee, tas,
                    toggleSubmitRoll, toggleSubmitLeaveSlip, toggleSubmitGroupLeaveSlip, toggleOtherReasons,
                    removeSelectedEvent, removeAllSelectedEvents, postRoll, postSlip, postRollSlip }) => {
  var disabledClass = 'remove-all';
  if (selectedEvents.length == 0) {
    disabledClass += ' disabled'
  }

  var showSection = {};
  if (submitRollShow) {
    showSection = {display: "none"};
  }

  var hideRoll = {};
  if (trainee.term[trainee.term.length-1] <= 2) {
    hideRoll = {display: "none"};
  }

  return (
    <div style={{marginBottom: "10px"}}>
    {/*Form control buttons*/}
      <div>
        <Button style={{marginRight: "8px"}} onClick={toggleSubmitRoll} style={hideRoll}>Roll</Button>
        <Button style={{marginRight: "8px"}} onClick={toggleSubmitLeaveSlip}>Leave Slip</Button>
        <Button style={{marginRight: "8px"}} onClick={toggleSubmitGroupLeaveSlip}>Group Leave Slip</Button>
      </div>
    {/*Sessions selected*/}
      <div>
        <Collapse in={selectedEvents.length > 0 || submitRollShow || submitLeaveSlipShow || submitGroupLeaveSlipShow}>
          <div className="form-body">
            <div className="form-section">
              <div className="toggle-title">
                Sessions Selected
                <Button bsSize="small" className={disabledClass} onClick={removeAllSelectedEvents}>Remove All</Button>
              </div>
              <div>
                {selectedEvents.map(function(ev) {
                  return <SelectedEvent
                            {...ev}
                            onClick={() => removeSelectedEvent(ev)}
                            selectedEvents={selectedEvents}
                          />
                })}
              </div>
            </div>
          </div>
        </Collapse>
      </div>
    {/*Roll and slip form*/}
      <div>
        <RollSlipForm
          post={(rollSlip) => postRollSlip(rollSlip, selectedEvents)}
          submitRollShow={submitRollShow}
          submitLeaveSlipShow={submitLeaveSlipShow}
          toggleSubmitLeaveSlip={() => toggleSubmitLeaveSlip()}
          toggleOtherReasons={() => toggleOtherReasons()}
          otherReasonsShow={otherReasonsShow}
          selectedEvents={selectedEvents}
          tas={tas}
          initialValues={{informStatus: "true"}}
        />
      </div>
    {/*Group slip form*/}
      <div>
        <Collapse in={submitGroupLeaveSlipShow}>
          <div className="form-body form-together">
              <div className="form-section">
                <div>
                  <div className="toggle-title">Trainees</div>
                  <textarea className="comments-textarea"></textarea>
                </div>
                <div className="toggle-title">Reason</div>
                <div data-toggle="buttons">
                  <div className="reason-container">
                    <label className="roll-input"><input type="radio" name="options" autoComplete="off"/> Fellowship </label>
                    <label className="roll-input"><input type="radio" name="options" autoComplete="off"/> Service </label>
                    <label className="roll-input"><input type="radio" name="options" autoComplete="off"/> Conference </label>
                    <label className="roll-input"><input type="radio" name="options" autoComplete="off"/> Gospel </label>
                    <label className="roll-input"><input type="radio" name="options" autoComplete="off"/> Night Out </label>
                    <span onClick={toggleOtherReasons} className="checkbox-container">
                      <input type="checkbox" checked={otherReasonsShow}/> Other <span className="caret"></span>
                    </span>
                    <Collapse in={otherReasonsShow}>
                      <div data-toggle="buttons">
                        <label className="roll-input"><input type="radio" name="options" autoComplete="off"/> Sickness </label>
                        <label className="roll-input"><input type="radio" name="options" autoComplete="off"/> Meal Out </label>
                        <label className="roll-input"><input type="radio" name="options" autoComplete="off"/> Interview </label>
                        <label className="roll-input"><input type="radio" name="options" autoComplete="off"/> Wedding </label>
                        <label className="roll-input"><input type="radio" name="options" autoComplete="off"/> Funeral </label>
                      </div>
                    </Collapse>
                  </div>
                  <div className="border-top">
                    <label className="notification-only"><input type="radio" name="options" autoComplete="off"/> Notification Only </label>
                  </div>
                </div>
                <div>
                  <div className="toggle-title">Comments</div>
                  <textarea className="comments-textarea"></textarea>
                </div>
                <div className="input-group">
                  <div className="input-group-btn">
                    <button type="button" className="btn btn-default dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">TA informed <span className="caret"></span></button>
                    <ul className="dropdown-menu">
                      <li><a href="#">TA informed</a></li>
                      <li><a href="#">Did not inform training office</a></li>
                      <li role="separator" className="divider"></li>
                      <OverlayTrigger placement="bottom" overlay={<Popover id="att-num-pop" style={{width: 200}}>For sisters during non-Front Office hours only</Popover>}>
                        <li><a href="#">Texted attendance number</a></li>
                      </OverlayTrigger>
                    </ul>
                  </div>
                  <input type="text" className="form-control" aria-label="..."/>
                </div>
            </div>
            </div>
        </Collapse>
      </div>
    </div>
  )
}

ActionBar.propTypes = {
  submitRollShow: PropTypes.bool.isRequired, 
  submitLeaveSlipShow: PropTypes.bool.isRequired, 
  submitGroupLeaveSlipShow: PropTypes.bool.isRequired,
  selectedEvents: PropTypes.arrayOf(PropTypes.object.isRequired).isRequired,
  toggleSubmitRoll: PropTypes.func.isRequired, 
  toggleSubmitLeaveSlip: PropTypes.func.isRequired, 
  toggleSubmitGroupLeaveSlip: PropTypes.func.isRequired
}

export default ActionBar
